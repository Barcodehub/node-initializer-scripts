import os
import subprocess
import shutil

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

def reemplazar_contenido_archivo(ruta_archivo, nuevo_contenido):
    """Reemplaza el contenido de un archivo con el nuevo contenido."""
    try:
        with open(ruta_archivo, "w") as f:
            f.write(nuevo_contenido)
        print(f"Archivo {ruta_archivo} actualizado correctamente.")
    except Exception as e:
        print(f"Error al actualizar el archivo {ruta_archivo}: {e}")
        exit(1)

def eliminar_linea_archivo(ruta_archivo, linea_a_eliminar):
    """Elimina una línea específica de un archivo."""
    try:
        with open(ruta_archivo, "r") as f:
            lineas = f.readlines()
        
        with open(ruta_archivo, "w") as f:
            for linea in lineas:
                if linea_a_eliminar not in linea:
                    f.write(linea)
        print(f"Línea eliminada de {ruta_archivo} correctamente.")
    except Exception as e:
        print(f"Error al eliminar la línea de {ruta_archivo}: {e}")
        exit(1)

def main():
    # Solicitar el nombre del proyecto
    project_name = input("Ingrese el nombre del proyecto: ")

    # Crear el proyecto con Vite, TypeScript y SWC
    ejecutar_comando(
        f"npm create vite@latest {project_name} -- --template react-swc-ts",
        mensaje_exito="Proyecto creado exitosamente.",
        mensaje_error="Error al crear el proyecto. Asegúrate de que npm y Node.js estén instalados."
    )

    # Navegar al directorio del proyecto
    os.chdir(project_name)

    # Eliminar archivos innecesarios
    if os.path.exists("src/App.css"):
        os.remove("src/App.css")
    if os.path.exists("src/assets"):
        shutil.rmtree("src/assets")
    print("Archivos innecesarios eliminados.")

    # Preguntar si se desea instalar Tailwind CSS
    tailwind_version = input("¿Desea instalar Tailwind CSS? (3/4/n): ").strip().lower()

    if tailwind_version in ["3", "4"]:
        if tailwind_version == "3":
            print("Instalando Tailwind CSS 3...")
            ejecutar_comando(
                "npm install -D tailwindcss@3 postcss autoprefixer",
                mensaje_exito="Tailwind CSS 3 instalado correctamente.",
                mensaje_error="Error al instalar Tailwind CSS 3."
            )
            ejecutar_comando("npx tailwindcss init")

            # Configurar postcss.config.js
            with open("postcss.config.js", "w") as f:
                f.write("""export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};""")

            # Configurar tailwind.config.js
            with open("tailwind.config.js", "w") as f:
                f.write("""/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{ts,tsx,js,jsx}"],
  theme: {
    extend: {},
  },
  plugins: [],
};""")

            # Configurar src/index.css
            with open("src/index.css", "w") as f:
                f.write("""@tailwind base;
@tailwind components;
@tailwind utilities;""")

        elif tailwind_version == "4":
            print("Instalando Tailwind CSS 4...")
            ejecutar_comando(
                "npm install tailwindcss @tailwindcss/postcss postcss",
                mensaje_exito="Tailwind CSS 4 instalado correctamente.",
                mensaje_error="Error al instalar Tailwind CSS 4."
            )

            # Configurar postcss.config.mjs
            with open("postcss.config.mjs", "w") as f:
                f.write("""export default {
  plugins: {
    "@tailwindcss/postcss": {},
  },
}""")

            # Configurar src/index.css
            with open("src/index.css", "w") as f:
                f.write("@import 'tailwindcss';")

    # Preguntar si se desea instalar react-router-dom
    instalar_router = input("¿Desea instalar react-router-dom? (s/n): ").strip().lower()

    if instalar_router == "s":
        print("Instalando react-router-dom...")
        ejecutar_comando(
            "npm i react-router-dom",
            mensaje_exito="react-router-dom instalado correctamente.",
            mensaje_error="Error al instalar react-router-dom."
        )

    # Reemplazar contenido de src/App.tsx
    nuevo_contenido_app = """function App() {

  return (
    <>
      <h1 className='text-amber-300 text-center'>hello world con Tailwind CSS</h1>
    </>
  )
}

export default App
"""
    reemplazar_contenido_archivo("src/App.tsx", nuevo_contenido_app)

    # Eliminar la importación de './index.css' en src/main.tsx
    eliminar_linea_archivo("src/main.tsx", "import './index.css'")

    # Instalar dependencias
    print("Instalando dependencias...")
    ejecutar_comando(
        "npm install",
        mensaje_exito="Dependencias instaladas correctamente.",
        mensaje_error="Error al instalar las dependencias."
    )

    print("¡Proyecto configurado exitosamente!")

if __name__ == "__main__":
    main()