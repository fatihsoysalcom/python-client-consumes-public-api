import urllib.request
import json

def get_post_data(post_id):
    """
    Simulates an application making a request to an API to get post data.
    """
    # This is the 'API Endpoint' - the specific address where the data can be requested.
    # Think of it as telling the 'waiter' (API) which dish you want from the 'kitchen' (server).
    api_url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    try:
        # The 'client application' sends a request to the 'API'.
        # It doesn't need to know how the data is stored or processed on the server side.
        # It just asks for 'post number X'.
        with urllib.request.urlopen(api_url) as response:
            # The 'API' (server) processes the request and sends back the data.
            data = response.read().decode('utf-8')
            post = json.loads(data) # The data is usually in JSON format.

            print(f"--- Data received for Post ID: {post_id} ---")
            print(f"Title: {post.get('title')}")
            print(f"Body: {post.get('body')[:100]}...") # Print first 100 chars of body
            print("--------------------------------------\n")
            return post
    except urllib.error.URLError as e:
        print(f"Error accessing the API: {e.reason}")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON response.")
        return None

if __name__ == "__main__":
    print("Demonstrating API interaction: Fetching data from a public API.")
    print("This script acts as a 'client application' requesting information from another 'service'.\n")

    # Request data for a specific post
    post1_data = get_post_data(1)
    if post1_data:
        print("Successfully fetched data for Post ID 1.")

    # Request data for another post
    post2_data = get_post_data(2)
    if post2_data:
        print("Successfully fetched data for Post ID 2.")

    # Demonstrate a non-existent post (API might return 404 or empty)
    print("\nAttempting to fetch data for a non-existent Post ID (9999)...")
    non_existent_post = get_post_data(9999)
    if not non_existent_post:
        print("As expected, no data or an error was returned for Post ID 9999, demonstrating API handling of invalid requests.")

    print("\nAPI interaction demonstration complete.")