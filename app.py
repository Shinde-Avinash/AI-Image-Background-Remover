import os
from rembg import remove
from PIL import Image
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template, send_from_directory

# --- Configuration ---
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'webp'])

# Ensure necessary directories exist
if 'static' not in os.listdir('.'):
    os.mkdir('static')

if 'uploads' not in os.listdir('static/'):
    os.mkdir('static/uploads')

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 # Prevent caching
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "super_secret_key" # Use a stronger key in production

# --- Utility Functions ---
def allowed_file(filename):
    """Checks if the file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def remove_background(input_path, output_path):
    """Opens an image, removes the background, and saves the result."""
    try:
        input_image = Image.open(input_path)
        output_image = remove(input_image)
        output_image.save(output_path)
    except Exception as e:
        print(f"Error during background removal: {e}")
        # Optionally, handle the error more gracefully here
        pass

# --- Routes ---

@app.route('/')
def home():
    """Renders the main upload page."""
    return render_template('home.html')

@app.route('/remback', methods=['POST'])
def remback():
    """Handles file upload and background removal."""
    if 'file' not in request.files:
        # User might not have selected a file
        return render_template('home.html', error_message='No file part in the request.')
    
    file = request.files['file']

    if file.filename == '':
        # User submitted without selecting a file
        return render_template('home.html', error_message='No selected file.')

    if file and allowed_file(file.filename):
        try:
            # Secure the filename and save the original file
            filename = secure_filename(file.filename)
            original_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(original_path)

            # Define the output path for the processed image
            name, ext = os.path.splitext(filename)
            rembg_img_name = f"{name}_rembg.png"
            output_path = os.path.join(app.config['UPLOAD_FOLDER'], rembg_img_name)
            
            # Process the image
            remove_background(original_path, output_path)

            # Render the page with results
            return render_template(
                'home.html',
                org_img_name=filename,
                rembg_img_name=rembg_img_name
            )
        except Exception as e:
            # Catch general errors during processing/saving
            print(f"An error occurred: {e}")
            return render_template('home.html', error_message=f'An error occurred during processing: {e}')
    else:
        # File type not allowed
        return render_template('home.html', error_message='File type not allowed. Use PNG, JPG, JPEG, or WEBP.')

if __name__ == '__main__':
    # Setting debug to True allows for immediate development feedback
    app.run(debug=True)