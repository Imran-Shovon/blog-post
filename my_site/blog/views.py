from datetime import date
from xml.dom.minidom import Identified

from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "title": "Mountain Hiking",
        "image": "mountain.jpg",
        "author": "Shovon",
        "date": date(2022, 7, 5),
        "excerpt": "My goal is to keep growing as a developer- and if I could help you do the same, I'd be very happy!",
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aut sint nesciunt
            libero fugit, inventore reprehenderit cumque quaerat totam asperiores eaque
            enim blanditiis voluptatum minus facere? Aspernatur, dolorem vel.
            Distinctio, ut!
            
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aut sint nesciunt
            libero fugit, inventore reprehenderit cumque quaerat totam asperiores eaque
            enim blanditiis voluptatum minus facere? Aspernatur, dolorem vel.
            Distinctio, ut!
            
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aut sint nesciunt
            libero fugit, inventore reprehenderit cumque quaerat totam asperiores eaque
            enim blanditiis voluptatum minus facere? Aspernatur, dolorem vel.
            Distinctio, ut!
        """
    },
    {
        "slug": "programming-is-fun",
        "title": "Programming Is Great",
        "image": "coding.png",
        "author": "Shovon",
        "date": date(2022, 7, 10),
        "excerpt": "Did you ever search an hour of your error? If you did then it's great for coding. Let's continue.",
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aut sint nesciunt
            libero fugit, inventore reprehenderit cumque quaerat totam asperiores eaque
            enim blanditiis voluptatum minus facere? Aspernatur, dolorem vel.
            Distinctio, ut!
            
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aut sint nesciunt
            libero fugit, inventore reprehenderit cumque quaerat totam asperiores eaque
            enim blanditiis voluptatum minus facere? Aspernatur, dolorem vel.
            Distinctio, ut!
            
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aut sint nesciunt
            libero fugit, inventore reprehenderit cumque quaerat totam asperiores eaque
            enim blanditiis voluptatum minus facere? Aspernatur, dolorem vel.
            Distinctio, ut!
        """
    },
    {
        "slug": "into-the-woods",
        "title": "Nature At It's Best",
        "image": "woods.jpg",
        "author": "Shovon",
        "date": date(2022, 7, 20),
        "excerpt": "Nature is amzing! The amount of inspirations I get when I walk into the forests.",
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aut sint nesciunt
            libero fugit, inventore reprehenderit cumque quaerat totam asperiores eaque
            enim blanditiis voluptatum minus facere? Aspernatur, dolorem vel.
            Distinctio, ut!
            
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aut sint nesciunt
            libero fugit, inventore reprehenderit cumque quaerat totam asperiores eaque
            enim blanditiis voluptatum minus facere? Aspernatur, dolorem vel.
            Distinctio, ut!
            
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aut sint nesciunt
            libero fugit, inventore reprehenderit cumque quaerat totam asperiores eaque
            enim blanditiis voluptatum minus facere? Aspernatur, dolorem vel.
            Distinctio, ut!
        """
    }
]

def get_date(post):
    return post['date']

# Create your views here.
def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html',{
        "posts": latest_posts,
    })

def posts(request):
    return render(request, 'blog/all-posts.html',{
        "all_posts": all_posts,
    })

def post_detail(request, slug):
    Identified_posts = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-details.html',{
        "post": Identified_posts
    })
