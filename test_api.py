import requests
import base64
from io import BytesIO
from PIL import Image

# Create a simple test image
def create_test_image():
    """Create a simple test image"""
    img = Image.new('RGB', (100, 100), color='red')
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    return buffer

# Test the API endpoint
def test_upload_api():
    url = 'http://rpbai.in/v1/upload_gpaiemail'

    # Create test data
    test_email = 'sohil@oizom.com'

    # Create a test image file
    image_file = create_test_image()

    # Prepare the form data
    files = {
        'image': ('test_badge.png', image_file, 'image/png')
    }

    data = {
        'email': test_email
    }

    print(f"Testing API: {url}")
    print(f"Email: {test_email}")
    print("Sending request...")

    try:
        response = requests.post(url, files=files, data=data)

        print(f"\nStatus Code: {response.status_code}")
        print(f"Response Headers: {response.headers}")
        print(f"Response Body: {response.text}")

        if response.status_code == 200:
            print("\n✅ API call successful!")
            try:
                json_response = response.json()
                print(f"JSON Response: {json_response}")
            except:
                print("Response is not JSON format")
        else:
            print(f"\n❌ API call failed with status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"\n❌ Error occurred: {e}")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")

if __name__ == "__main__":
    # Check if requests library is installed
    try:
        import requests
        from PIL import Image
        test_upload_api()
    except ImportError as e:
        print(f"Missing required library: {e}")
        print("\nPlease install required libraries:")
        print("pip install requests pillow")
