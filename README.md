# WebEmpresarial Django

Este es un proyecto Django diseñado para ser un sitio web empresarial básico. Permite la creación y gestión de páginas de contenido y cuenta con un formulario de contacto funcional.

## Características Principales

*   **Gestión de Páginas Dinámicas**:
    *   Creación de páginas con títulos y contenido enriquecido (usando CKEditor).
    *   Ordenamiento personalizado de las páginas.
    *   Administración sencilla a través del panel de Django admin.
*   **Formulario de Contacto**:
    *   Permite a los visitantes enviar mensajes a través de un formulario.
    *   Validación de campos (nombre, email, contenido).
    *   Envío de los mensajes por correo electrónico.
*   **Diseño Responsivo (implícito)**: Aunque no se especifica, los `form-control` de Bootstrap sugieren una base para un diseño adaptable.

## Aplicaciones (Apps) del Proyecto

1.  **`pages`**:
    *   Gestiona las páginas estáticas/informativas del sitio web.
    *   Modelo `Page` con campos para título, contenido (RichTextField), orden, y fechas de creación/actualización.
    *   Vista para mostrar el contenido de una página específica.
2.  **`contact`**:
    *   Implementa la funcionalidad del formulario de contacto.
    *   `ContactForm` para la captura y validación de datos del usuario.
    *   Vista para procesar el formulario y enviar un correo electrónico con los detalles del contacto.

## Tecnologías Clave

*   **Python**
*   **Django**
*   **CKEditor**: Para el campo de contenido enriquecido en las páginas.
*   **HTML/CSS/JavaScript** (a través de las plantillas de Django y widgets de formulario)

## Instalación y Puesta en Marcha (General)

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/tu-usuario/WebEmpresarial.git
    cd WebEmpresarial
    ```
2.  **Crear y activar un entorno virtual:**
    ```bash
    python -m venv venv
    # En Windows
    venv\Scripts\activate
    # En macOS/Linux
    source venv/bin/activate
    ```
3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Nota: Asegúrate de tener un archivo `requirements.txt` con Django, Pillow, django-ckeditor, etc.)*

4.  **Realizar migraciones:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5.  **Crear un superusuario (para acceder al admin):**
    ```bash
    python manage.py createsuperuser
    ```
6.  **Ejecutar el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```
    El sitio estará disponible en `http://127.0.0.1:8000/`.
    El panel de administración en `http://127.0.0.1:8000/admin/`.

## Configuración Adicional

*   **Correo Electrónico**: La configuración para el envío de correos (actualmente usando `mailtrap.io` como placeholder en `contact/views.py`) deberá ser ajustada en `settings.py` para un entorno de producción (ej. usando SendGrid, Gmail SMTP, etc.).

---

Este proyecto sirve como una base sólida para un sitio web corporativo o informativo, con funcionalidades esenciales ya implementadas.
