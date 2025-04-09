# app/generators/file_builder.py

import os
from jinja2 import Environment, FileSystemLoader
from app.database.db_session import SessionLocal
from app.models.crud import CrudModel, CrudField

# 📁 Template papkasini ko‘rsatamiz
template_dir = os.path.join(os.path.dirname(__file__))
env = Environment(loader=FileSystemLoader(template_dir))

# 🔌 DB sessiyasi
db = SessionLocal()

def generate_code_files(crud_id: int):
    crud = db.query(CrudModel).filter(CrudModel.id == crud_id).first()
    if not crud:
        raise Exception("CRUD not found")

    fields = db.query(CrudField).filter(CrudField.crud_id == crud_id).all()

    # 🧱 SQLAlchemy uchun tur konversiyasi
    def map_sqlalchemy_type(ftype: str):
        mapping = {
            "String": "String",
            "Integer": "Integer",
            "Boolean": "Boolean",
            "UUID": "UUID"
        }
        return mapping.get(ftype, "String")

    def map_python_type(ftype: str):
        mapping = {
            "String": "str",
            "Integer": "int",
            "Boolean": "bool",
            "UUID": "str"
        }
        return mapping.get(ftype, "str")

    sqlalchemy_imports = list(set([map_sqlalchemy_type(f.type) for f in fields]))

    extra_imports = []
    for f in fields:
        if f.format and "uuid4()" in f.format:
            extra_imports.append("from uuid import uuid4")


    render_data = {
    "model_name": crud.name,
    "table_name": crud.name.lower(),
    "imports": sqlalchemy_imports,
    "extra_imports": extra_imports,
    "fields": [
        {
            "name": f.name,
            "type": map_sqlalchemy_type(f.type),
            "nullable": f.nullable,
            "format": f.format,
            "python_type": map_python_type(f.type)
        }
        for f in fields
    ]
}


    # 📁 Saqlash yo‘llari
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    files = {
        f"models/{crud.name}.py": "model_template.jinja2",
        f"schemas/{crud.name}.py": "schema_template.jinja2",
        f"routers/{crud.name}.py": "router_template.jinja2",
    }

    for file_path, template_file in files.items():
        template = env.get_template(template_file)
        content = template.render(render_data)

        full_path = os.path.join(base_path, file_path)
        with open(full_path, "w") as f:
            f.write(content)
            print(f"[+] Created: {full_path}")
