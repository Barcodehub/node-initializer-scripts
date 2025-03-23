import os
import subprocess

def ejecutar_comando(comando, mensaje_exito=None, mensaje_error=None):
    """Ejecuta un comando en la terminal y maneja errores."""
    try:
        subprocess.run(comando, shell=True, check=True)
        if mensaje_exito:
            print(mensaje_exito)
    except subprocess.CalledProcessError as e:
        if mensaje_error:
            print(mensaje_error)
        print(f"Error: {e}")
        exit(1)

def crear_archivo(ruta, contenido):
    """Crea un archivo con el contenido especificado."""
    try:
        with open(ruta, "w") as f:
            f.write(contenido)
        print(f"Archivo {ruta} creado correctamente.")
    except Exception as e:
        print(f"Error al crear el archivo {ruta}: {e}")
        exit(1)

def main():
    # Solicitar el nombre del proyecto
    project_name = input("Ingrese el nombre del proyecto: ")

    # Crear el directorio del proyecto
    os.makedirs(project_name, exist_ok=True)
    os.chdir(project_name)

    # Inicializar el proyecto con npm
    ejecutar_comando(
        "npm init -y",
        mensaje_exito="Proyecto inicializado con npm.",
        mensaje_error="Error al inicializar el proyecto con npm."
    )

    # Instalar dependencias principales
    ejecutar_comando(
        "npm install express",
        mensaje_exito="Express instalado correctamente.",
        mensaje_error="Error al instalar Express."
    )

    # Instalar dependencias de desarrollo
    ejecutar_comando(
        "npm install -D typescript ts-node nodemon @types/node @types/express @types/cors",
        mensaje_exito="Dependencias de desarrollo instaladas correctamente.",
        mensaje_error="Error al instalar dependencias de desarrollo."
    )

    # Inicializar TypeScript
    ejecutar_comando(
        "npx tsc --init",
        mensaje_exito="TypeScript inicializado correctamente.",
        mensaje_error="Error al inicializar TypeScript."
    )

    # Crear el archivo tsconfig.json
    tsconfig_content = """{
    "compilerOptions": {
        "outDir": "./dist",
        "rootDir": "./src",
        "lib": ["ESNext"],
        "target": "ESNext",
        "moduleResolution": "nodenext",
        "module": "NodeNext",
        "strict": false,
        "sourceMap": true,
        "esModuleInterop": true,
        "declaration": true
    },
    "include": ["src/**/*.ts"]
}"""
    crear_archivo("tsconfig.json", tsconfig_content)

    # Crear la estructura de directorios
    os.makedirs("src", exist_ok=True)

    # Crear el archivo index.ts
    index_ts_content = """import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';

dotenv.config();

const app = express();
app.use(cors());
app.use(express.json());

app.get('/', (req, res) => {
    res.send('Hola mundo');
});

const port = process.env.PORT || 4000;

app.listen(port, () => {
    console.log('Servidor funcionando en el puerto', port);
});"""
    crear_archivo("src/index.ts", index_ts_content)

    # Actualizar package.json con los scripts
    with open("package.json", "r") as f:
        package_json = f.read()

    package_json = package_json.replace(
        '"test": "echo \\"Error: no test specified\\" && exit 1"',
        '"dev": "nodemon src/index.ts",\n    "build": "tsc",\n    "start": "node dist/index.js"'
    )

    with open("package.json", "w") as f:
        f.write(package_json)
    print("Scripts actualizados en package.json.")

    # Instalar dependencias adicionales
    ejecutar_comando(
        "npm install mongoose dotenv cors",
        mensaje_exito="Dependencias adicionales instaladas correctamente.",
        mensaje_error="Error al instalar dependencias adicionales."
    )

    print("¡Proyecto configurado exitosamente!")

if __name__ == "__main__":
    main()