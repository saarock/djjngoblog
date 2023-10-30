from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator
from .models import Comment, Contact_us
from rest_framework.decorators import api_view

api_for_blogs = [
    {"id": 0,
     "image": "https://media.istockphoto.com/id/1371339413/photo/co-working-team-meeting-concept-businessman-using-smart-phone-and-digital-tablet-and-laptop.webp?s=2048x2048&w=is&k=20&c=k0HGlKZDGIpAIQCx4RUEjdT-KlPoPx5iJyU6QQt9O-8=",
     "title": "How to Learn python progrmming langauge. ",
     "extra": "As one of the most popular programming languages out there, many people want to learn Python. But how do you go about getting started? In this guide, we explore everything you need to know to begin your learning journey, including a step-by-step guide and learning plan and some of the most useful resources to help you succeed.",
     "content1_title": "What is Python?",
     "content": "Python is a high-level, interpreted programming language created by Guido van Rossum and first released in 1991. It is designed with an emphasis on code readability, and its syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C++ or Java.",
     "content1_": "Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming. In simpler terms, this means it’s flexible and allows you to write code in different ways, whether that's like giving the computer a to-do list (procedural), creating digital models of things or concepts (object-oriented), or treating your code like a math problem (functional).",
     "content2_title": "What makes Python so popular?",
     "content2": "As of July 2023, Python remains the most popular programing language according to the TIOBE index. Over the years, Python has become one of the most popular programming languages due to its simplicity, versatility, and wide range of applications",
     "content2image": "https://images.datacamp.com/image/upload/v1688732584/image_bcd7581290.png",
     "content2_": "These reasons also mean it is a highly favored language for data science as it allows data scientists to focus more on data interpretation rather than language complexities.",
     "content2__": "Let’s explore these factors in more..",
     "content3_title": "The main features of Python",
     "features": [
         {
              "title": "Readability.",
             "content": " Python is known for its clear and readable syntax, which resembles English to a certain extent.",
         },
         {
             "title": "Easy to learn.",
             "content": "Python’s readability makes it relatively easy for beginners to pick up the language and understand what the code is doing.",
         },
         {
             "title": "Versatility. ",
             "content": "Python is not limited to one type of task; you can use it in many fields. Whether you're interested in web development, automating tasks, or diving into data science, Python has the tools to help you get there."
         },
         {
             "title": "Rich library support.",
             "content": "It comes with a large standard library that includes pre-written code for various tasks, saving you time and effort. Additionally, Python's vibrant community has developed thousands of third-party packages, which extend Python's functionality even further."
         },

         {
             "title": "Platform independence. ",
             "content": "One of the great things about the language is that you can write your code once and run it on any operating system. This feature makes Python a great choice if you're working on a team with different operating systems."
         },

         {
             "title": "Interpreted language.",
             "content": " Python is an interpreted language, which means the code is executed line by line. This can make debugging easier because you can test small pieces of code without having to compile the whole program."
         },

         {
             "title": "Open source and free",
             "content": "It’s also an open-source language, which means its source code is freely available and can be distributed and modified. This has led to a large community of developers contributing to its development and creating a vast ecosystem of Python libraries."
         },
         {
             "title": "Dynamically typed. ",
             #  "title": "",
             "content": "Python is dynamically typed, meaning you don't have to declare the data type of a variable when you create it. The Python interpreter infers the type, which makes the code more flexible and easy to work with.",
         }

     ],

     "content4_title": "An Example Python Learning Plan",
     "content4": "Below, we’ve created a potential learning plan outlining where to focus your time and efforts if you’re just starting out with Python. Remember, the timescales, subject areas, and progress all depend on a wide range of variables. We want to make this plan as hands-on and practical as possible, which is why we’ve recommended projects you can work on as you progress.",
     "content5_title": "Month 1-3: Basics of Python and data manipulation",
     "content5": "Master basic and intermediate programming concepts. Start doing basic projects in your specialized field. For example, if you're interested in data science, you might start by analyzing a dataset using pandas and visualizing the data with matplotlib.",
     "howtolearn": [
         {
             "title": "Python basics",
             "content": "Start with the fundamentals of Python. This includes understanding the syntax, data types, control structures, functions, and more."
         },
         {
             "title": "Data manipulation",
             "content": " Learn how to handle and manipulate data using Python libraries like pandas and NumPy. This is a crucial skill for any Python-related job, especially in data science and machine learning."
         }
     ]

     },

    {"id": 1,
     #  "image": "https://media.istockphoto.com/id/1371339413/photo/co-working-team-meeting-concept-businessman-using-smart-phone-and-digital-tablet-and-laptop.webp?s=2048x2048&w=is&k=20&c=k0HGlKZDGIpAIQCx4RUEjdT-KlPoPx5iJyU6QQt9O-8=",
     "title": "How to learn the python in the 2023?",
     "content": "This is the first blog post.Lorem Ipsum is simply dummy text of the printing and typesetting jsadbfgsdfsad gasudghsadug asdghasuidg asdgiuasdghusaid gasdiuughasdugha sdgasdghasdughasdughasd gasdughasdugh asdgasdhgasudg asdugahgasduigasdui ga",

     "image": "data:image/jpeg;base64,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"
     },

]


api_blogs_popular_only = [
    {"id": 0,
     "image": "https://media.istockphoto.com/id/1371339413/photo/co-working-team-meeting-concept-businessman-using-smart-phone-and-digital-tablet-and-laptop.webp?s=2048x2048&w=is&k=20&c=k0HGlKZDGIpAIQCx4RUEjdT-KlPoPx5iJyU6QQt9O-8=",
     "title": "How to Be a Fullstack developer in 2023 and how to learn the HTML, CSS, javaScript and one backend langauge that can be any nodeJs,PHP, python and java? ",
     "extra": "As one of the most popular programming languages out there, many people want to learn Python. But how do you go about getting started? In this guide, we explore everything you need to know to begin your learning journey, including a step-by-step guide and learning plan and some of the most useful resources to help you succeed.",
     "content1_title": "What is Python?",
     "content1": "Python is a high-level, interpreted programming language created by Guido van Rossum and first released in 1991. It is designed with an emphasis on code readability, and its syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C++ or Java.",
     "content1_": "Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming. In simpler terms, this means it’s flexible and allows you to write code in different ways, whether that's like giving the computer a to-do list (procedural), creating digital models of things or concepts (object-oriented), or treating your code like a math problem (functional).",
     "content2_title": "What makes Python so popular?",
     "content2": "As of July 2023, Python remains the most popular programing language according to the TIOBE index. Over the years, Python has become one of the most popular programming languages due to its simplicity, versatility, and wide range of applications",
     "content2image": "https://images.datacamp.com/image/upload/v1688732584/image_bcd7581290.png",
     "content2_": "These reasons also mean it is a highly favored language for data science as it allows data scientists to focus more on data interpretation rather than language complexities.",
     "content2__": "Let’s explore these factors in more..",
     "content3_title": "The main features of Python",
     "features": [
         {
              "title": "Readability.",
             "content": " Python is known for its clear and readable syntax, which resembles English to a certain extent.",
         },
         {
             "title": "Easy to learn.",
             "content": "Python’s readability makes it relatively easy for beginners to pick up the language and understand what the code is doing.",
         },
         {
             "title": "Versatility. ",
             "content": "Python is not limited to one type of task; you can use it in many fields. Whether you're interested in web development, automating tasks, or diving into data science, Python has the tools to help you get there."
         },
         {
             "title": "Rich library support.",
             "content": "It comes with a large standard library that includes pre-written code for various tasks, saving you time and effort. Additionally, Python's vibrant community has developed thousands of third-party packages, which extend Python's functionality even further."
         },

         {
             "title": "Platform independence. ",
             "content": "One of the great things about the language is that you can write your code once and run it on any operating system. This feature makes Python a great choice if you're working on a team with different operating systems."
         },

         {
             "title": "Interpreted language.",
             "content": " Python is an interpreted language, which means the code is executed line by line. This can make debugging easier because you can test small pieces of code without having to compile the whole program."
         },

         {
             "title": "Open source and free",
             "content": "It’s also an open-source language, which means its source code is freely available and can be distributed and modified. This has led to a large community of developers contributing to its development and creating a vast ecosystem of Python libraries."
         },
         {
             "title": "Dynamically typed. ",
             #  "title": "",
             "content": "Python is dynamically typed, meaning you don't have to declare the data type of a variable when you create it. The Python interpreter infers the type, which makes the code more flexible and easy to work with.",
         }

     ],

     "content4_title": "An Example Python Learning Plan",
     "content4": "Below, we’ve created a potential learning plan outlining where to focus your time and efforts if you’re just starting out with Python. Remember, the timescales, subject areas, and progress all depend on a wide range of variables. We want to make this plan as hands-on and practical as possible, which is why we’ve recommended projects you can work on as you progress.",
     "content5_title": "Month 1-3: Basics of Python and data manipulation",
     "content5": "Master basic and intermediate programming concepts. Start doing basic projects in your specialized field. For example, if you're interested in data science, you might start by analyzing a dataset using pandas and visualizing the data with matplotlib.",
     "howtolearn": [
         {
             "title": "Python basics",
             "content": "Start with the fundamentals of Python. This includes understanding the syntax, data types, control structures, functions, and more."
         },
         {
             "title": "Data manipulation",
             "content": " Learn how to handle and manipulate data using Python libraries like pandas and NumPy. This is a crucial skill for any Python-related job, especially in data science and machine learning."
         }
     ]

     },


       {"id": 0,
     "image": "https://media.istockphoto.com/id/1371339413/photo/co-working-team-meeting-concept-businessman-using-smart-phone-and-digital-tablet-and-laptop.webp?s=2048x2048&w=is&k=20&c=k0HGlKZDGIpAIQCx4RUEjdT-KlPoPx5iJyU6QQt9O-8=",
     "title": "How to Be a Fullstack developer in 2023 and how to learn the HTML, CSS, javaScript and one backend langauge that can be any nodeJs,PHP, python and java? ",
     "extra": "As one of the most popular programming languages out there, many people want to learn Python. But how do you go about getting started? In this guide, we explore everything you need to know to begin your learning journey, including a step-by-step guide and learning plan and some of the most useful resources to help you succeed.",
     "content1_title": "What is Python?",
     "content1": "Python is a high-level, interpreted programming language created by Guido van Rossum and first released in 1991. It is designed with an emphasis on code readability, and its syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C++ or Java.",
     "content1_": "Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming. In simpler terms, this means it’s flexible and allows you to write code in different ways, whether that's like giving the computer a to-do list (procedural), creating digital models of things or concepts (object-oriented), or treating your code like a math problem (functional).",
     "content2_title": "What makes Python so popular?",
     "content2": "As of July 2023, Python remains the most popular programing language according to the TIOBE index. Over the years, Python has become one of the most popular programming languages due to its simplicity, versatility, and wide range of applications",
     "content2image": "https://images.datacamp.com/image/upload/v1688732584/image_bcd7581290.png",
     "content2_": "These reasons also mean it is a highly favored language for data science as it allows data scientists to focus more on data interpretation rather than language complexities.",
     "content2__": "Let’s explore these factors in more..",
     "content3_title": "The main features of Python",
     "features": [
         {
              "title": "Readability.",
             "content": " Python is known for its clear and readable syntax, which resembles English to a certain extent.",
         },
         {
             "title": "Easy to learn.",
             "content": "Python’s readability makes it relatively easy for beginners to pick up the language and understand what the code is doing.",
         },
         {
             "title": "Versatility. ",
             "content": "Python is not limited to one type of task; you can use it in many fields. Whether you're interested in web development, automating tasks, or diving into data science, Python has the tools to help you get there."
         },
         {
             "title": "Rich library support.",
             "content": "It comes with a large standard library that includes pre-written code for various tasks, saving you time and effort. Additionally, Python's vibrant community has developed thousands of third-party packages, which extend Python's functionality even further."
         },

         {
             "title": "Platform independence. ",
             "content": "One of the great things about the language is that you can write your code once and run it on any operating system. This feature makes Python a great choice if you're working on a team with different operating systems."
         },

         {
             "title": "Interpreted language.",
             "content": " Python is an interpreted language, which means the code is executed line by line. This can make debugging easier because you can test small pieces of code without having to compile the whole program."
         },

         {
             "title": "Open source and free",
             "content": "It’s also an open-source language, which means its source code is freely available and can be distributed and modified. This has led to a large community of developers contributing to its development and creating a vast ecosystem of Python libraries."
         },
         {
             "title": "Dynamically typed. ",
             #  "title": "",
             "content": "Python is dynamically typed, meaning you don't have to declare the data type of a variable when you create it. The Python interpreter infers the type, which makes the code more flexible and easy to work with.",
         }

     ],

     "content4_title": "An Example Python Learning Plan",
     "content4": "Below, we’ve created a potential learning plan outlining where to focus your time and efforts if you’re just starting out with Python. Remember, the timescales, subject areas, and progress all depend on a wide range of variables. We want to make this plan as hands-on and practical as possible, which is why we’ve recommended projects you can work on as you progress.",
     "content5_title": "Month 1-3: Basics of Python and data manipulation",
     "content5": "Master basic and intermediate programming concepts. Start doing basic projects in your specialized field. For example, if you're interested in data science, you might start by analyzing a dataset using pandas and visualizing the data with matplotlib.",
     "howtolearn": [
         {
             "title": "Python basics",
             "content": "Start with the fundamentals of Python. This includes understanding the syntax, data types, control structures, functions, and more."
         },
         {
             "title": "Data manipulation",
             "content": " Learn how to handle and manipulate data using Python libraries like pandas and NumPy. This is a crucial skill for any Python-related job, especially in data science and machine learning."
         }
     ]

     },


       {"id": 0,
     "image": "https://media.istockphoto.com/id/1371339413/photo/co-working-team-meeting-concept-businessman-using-smart-phone-and-digital-tablet-and-laptop.webp?s=2048x2048&w=is&k=20&c=k0HGlKZDGIpAIQCx4RUEjdT-KlPoPx5iJyU6QQt9O-8=",
     "title": "How to Be a Fullstack developer in 2023 and how to learn the HTML, CSS, javaScript and one backend langauge that can be any nodeJs,PHP, python and java? ",
     "extra": "As one of the most popular programming languages out there, many people want to learn Python. But how do you go about getting started? In this guide, we explore everything you need to know to begin your learning journey, including a step-by-step guide and learning plan and some of the most useful resources to help you succeed.",
     "content1_title": "What is Python?",
     "content1": "Python is a high-level, interpreted programming language created by Guido van Rossum and first released in 1991. It is designed with an emphasis on code readability, and its syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C++ or Java.",
     "content1_": "Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming. In simpler terms, this means it’s flexible and allows you to write code in different ways, whether that's like giving the computer a to-do list (procedural), creating digital models of things or concepts (object-oriented), or treating your code like a math problem (functional).",
     "content2_title": "What makes Python so popular?",
     "content2": "As of July 2023, Python remains the most popular programing language according to the TIOBE index. Over the years, Python has become one of the most popular programming languages due to its simplicity, versatility, and wide range of applications",
     "content2image": "https://images.datacamp.com/image/upload/v1688732584/image_bcd7581290.png",
     "content2_": "These reasons also mean it is a highly favored language for data science as it allows data scientists to focus more on data interpretation rather than language complexities.",
     "content2__": "Let’s explore these factors in more..",
     "content3_title": "The main features of Python",
     "features": [
         {
              "title": "Readability.",
             "content": " Python is known for its clear and readable syntax, which resembles English to a certain extent.",
         },
         {
             "title": "Easy to learn.",
             "content": "Python’s readability makes it relatively easy for beginners to pick up the language and understand what the code is doing.",
         },
         {
             "title": "Versatility. ",
             "content": "Python is not limited to one type of task; you can use it in many fields. Whether you're interested in web development, automating tasks, or diving into data science, Python has the tools to help you get there."
         },
         {
             "title": "Rich library support.",
             "content": "It comes with a large standard library that includes pre-written code for various tasks, saving you time and effort. Additionally, Python's vibrant community has developed thousands of third-party packages, which extend Python's functionality even further."
         },

         {
             "title": "Platform independence. ",
             "content": "One of the great things about the language is that you can write your code once and run it on any operating system. This feature makes Python a great choice if you're working on a team with different operating systems."
         },

         {
             "title": "Interpreted language.",
             "content": " Python is an interpreted language, which means the code is executed line by line. This can make debugging easier because you can test small pieces of code without having to compile the whole program."
         },

         {
             "title": "Open source and free",
             "content": "It’s also an open-source language, which means its source code is freely available and can be distributed and modified. This has led to a large community of developers contributing to its development and creating a vast ecosystem of Python libraries."
         },
         {
             "title": "Dynamically typed. ",
             #  "title": "",
             "content": "Python is dynamically typed, meaning you don't have to declare the data type of a variable when you create it. The Python interpreter infers the type, which makes the code more flexible and easy to work with.",
         }

     ],

     "content4_title": "An Example Python Learning Plan",
     "content4": "Below, we’ve created a potential learning plan outlining where to focus your time and efforts if you’re just starting out with Python. Remember, the timescales, subject areas, and progress all depend on a wide range of variables. We want to make this plan as hands-on and practical as possible, which is why we’ve recommended projects you can work on as you progress.",
     "content5_title": "Month 1-3: Basics of Python and data manipulation",
     "content5": "Master basic and intermediate programming concepts. Start doing basic projects in your specialized field. For example, if you're interested in data science, you might start by analyzing a dataset using pandas and visualizing the data with matplotlib.",
     "howtolearn": [
         {
             "title": "Python basics",
             "content": "Start with the fundamentals of Python. This includes understanding the syntax, data types, control structures, functions, and more."
         },
         {
             "title": "Data manipulation",
             "content": " Learn how to handle and manipulate data using Python libraries like pandas and NumPy. This is a crucial skill for any Python-related job, especially in data science and machine learning."
         }
     ]

     },



       {"id": 0,
     "image": "https://media.istockphoto.com/id/1371339413/photo/co-working-team-meeting-concept-businessman-using-smart-phone-and-digital-tablet-and-laptop.webp?s=2048x2048&w=is&k=20&c=k0HGlKZDGIpAIQCx4RUEjdT-KlPoPx5iJyU6QQt9O-8=",
     "title": "How to Be a Fullstack developer in 2023 and how to learn the HTML, CSS, javaScript and one backend langauge that can be any nodeJs,PHP, python and java? ",
     "extra": "As one of the most popular programming languages out there, many people want to learn Python. But how do you go about getting started? In this guide, we explore everything you need to know to begin your learning journey, including a step-by-step guide and learning plan and some of the most useful resources to help you succeed.",
     "content1_title": "What is Python?",
     "content1": "Python is a high-level, interpreted programming language created by Guido van Rossum and first released in 1991. It is designed with an emphasis on code readability, and its syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C++ or Java.",
     "content1_": "Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming. In simpler terms, this means it’s flexible and allows you to write code in different ways, whether that's like giving the computer a to-do list (procedural), creating digital models of things or concepts (object-oriented), or treating your code like a math problem (functional).",
     "content2_title": "What makes Python so popular?",
     "content2": "As of July 2023, Python remains the most popular programing language according to the TIOBE index. Over the years, Python has become one of the most popular programming languages due to its simplicity, versatility, and wide range of applications",
     "content2image": "https://images.datacamp.com/image/upload/v1688732584/image_bcd7581290.png",
     "content2_": "These reasons also mean it is a highly favored language for data science as it allows data scientists to focus more on data interpretation rather than language complexities.",
     "content2__": "Let’s explore these factors in more..",
     "content3_title": "The main features of Python",
     "features": [
         {
              "title": "Readability.",
             "content": " Python is known for its clear and readable syntax, which resembles English to a certain extent.",
         },
         {
             "title": "Easy to learn.",
             "content": "Python’s readability makes it relatively easy for beginners to pick up the language and understand what the code is doing.",
         },
         {
             "title": "Versatility. ",
             "content": "Python is not limited to one type of task; you can use it in many fields. Whether you're interested in web development, automating tasks, or diving into data science, Python has the tools to help you get there."
         },
         {
             "title": "Rich library support.",
             "content": "It comes with a large standard library that includes pre-written code for various tasks, saving you time and effort. Additionally, Python's vibrant community has developed thousands of third-party packages, which extend Python's functionality even further."
         },

         {
             "title": "Platform independence. ",
             "content": "One of the great things about the language is that you can write your code once and run it on any operating system. This feature makes Python a great choice if you're working on a team with different operating systems."
         },

         {
             "title": "Interpreted language.",
             "content": " Python is an interpreted language, which means the code is executed line by line. This can make debugging easier because you can test small pieces of code without having to compile the whole program."
         },

         {
             "title": "Open source and free",
             "content": "It’s also an open-source language, which means its source code is freely available and can be distributed and modified. This has led to a large community of developers contributing to its development and creating a vast ecosystem of Python libraries."
         },
         {
             "title": "Dynamically typed. ",
             #  "title": "",
             "content": "Python is dynamically typed, meaning you don't have to declare the data type of a variable when you create it. The Python interpreter infers the type, which makes the code more flexible and easy to work with.",
         }

     ],

     "content4_title": "An Example Python Learning Plan",
     "content4": "Below, we’ve created a potential learning plan outlining where to focus your time and efforts if you’re just starting out with Python. Remember, the timescales, subject areas, and progress all depend on a wide range of variables. We want to make this plan as hands-on and practical as possible, which is why we’ve recommended projects you can work on as you progress.",
     "content5_title": "Month 1-3: Basics of Python and data manipulation",
     "content5": "Master basic and intermediate programming concepts. Start doing basic projects in your specialized field. For example, if you're interested in data science, you might start by analyzing a dataset using pandas and visualizing the data with matplotlib.",
     "howtolearn": [
         {
             "title": "Python basics",
             "content": "Start with the fundamentals of Python. This includes understanding the syntax, data types, control structures, functions, and more."
         },
         {
             "title": "Data manipulation",
             "content": " Learn how to handle and manipulate data using Python libraries like pandas and NumPy. This is a crucial skill for any Python-related job, especially in data science and machine learning."
         }
     ]

     },


       {"id": 0,
     "image": "https://media.istockphoto.com/id/1371339413/photo/co-working-team-meeting-concept-businessman-using-smart-phone-and-digital-tablet-and-laptop.webp?s=2048x2048&w=is&k=20&c=k0HGlKZDGIpAIQCx4RUEjdT-KlPoPx5iJyU6QQt9O-8=",
     "title": "How to Be a Fullstack developer in 2023 and how to learn the HTML, CSS, javaScript and one backend langauge that can be any nodeJs,PHP, python and java? ",
     "extra": "As one of the most popular programming languages out there, many people want to learn Python. But how do you go about getting started? In this guide, we explore everything you need to know to begin your learning journey, including a step-by-step guide and learning plan and some of the most useful resources to help you succeed.",
     "content1_title": "What is Python?",
     "content1": "Python is a high-level, interpreted programming language created by Guido van Rossum and first released in 1991. It is designed with an emphasis on code readability, and its syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C++ or Java.",
     "content1_": "Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming. In simpler terms, this means it’s flexible and allows you to write code in different ways, whether that's like giving the computer a to-do list (procedural), creating digital models of things or concepts (object-oriented), or treating your code like a math problem (functional).",
     "content2_title": "What makes Python so popular?",
     "content2": "As of July 2023, Python remains the most popular programing language according to the TIOBE index. Over the years, Python has become one of the most popular programming languages due to its simplicity, versatility, and wide range of applications",
     "content2image": "https://images.datacamp.com/image/upload/v1688732584/image_bcd7581290.png",
     "content2_": "These reasons also mean it is a highly favored language for data science as it allows data scientists to focus more on data interpretation rather than language complexities.",
     "content2__": "Let’s explore these factors in more..",
     "content3_title": "The main features of Python",
     "features": [
         {
              "title": "Readability.",
             "content": " Python is known for its clear and readable syntax, which resembles English to a certain extent.",
         },
         {
             "title": "Easy to learn.",
             "content": "Python’s readability makes it relatively easy for beginners to pick up the language and understand what the code is doing.",
         },
         {
             "title": "Versatility. ",
             "content": "Python is not limited to one type of task; you can use it in many fields. Whether you're interested in web development, automating tasks, or diving into data science, Python has the tools to help you get there."
         },
         {
             "title": "Rich library support.",
             "content": "It comes with a large standard library that includes pre-written code for various tasks, saving you time and effort. Additionally, Python's vibrant community has developed thousands of third-party packages, which extend Python's functionality even further."
         },

         {
             "title": "Platform independence. ",
             "content": "One of the great things about the language is that you can write your code once and run it on any operating system. This feature makes Python a great choice if you're working on a team with different operating systems."
         },

         {
             "title": "Interpreted language.",
             "content": " Python is an interpreted language, which means the code is executed line by line. This can make debugging easier because you can test small pieces of code without having to compile the whole program."
         },

         {
             "title": "Open source and free",
             "content": "It’s also an open-source language, which means its source code is freely available and can be distributed and modified. This has led to a large community of developers contributing to its development and creating a vast ecosystem of Python libraries."
         },
         {
             "title": "Dynamically typed. ",
             #  "title": "",
             "content": "Python is dynamically typed, meaning you don't have to declare the data type of a variable when you create it. The Python interpreter infers the type, which makes the code more flexible and easy to work with.",
         }

     ],

     "content4_title": "An Example Python Learning Plan",
     "content4": "Below, we’ve created a potential learning plan outlining where to focus your time and efforts if you’re just starting out with Python. Remember, the timescales, subject areas, and progress all depend on a wide range of variables. We want to make this plan as hands-on and practical as possible, which is why we’ve recommended projects you can work on as you progress.",
     "content5_title": "Month 1-3: Basics of Python and data manipulation",
     "content5": "Master basic and intermediate programming concepts. Start doing basic projects in your specialized field. For example, if you're interested in data science, you might start by analyzing a dataset using pandas and visualizing the data with matplotlib.",
     "howtolearn": [
         {
             "title": "Python basics",
             "content": "Start with the fundamentals of Python. This includes understanding the syntax, data types, control structures, functions, and more."
         },
         {
             "title": "Data manipulation",
             "content": " Learn how to handle and manipulate data using Python libraries like pandas and NumPy. This is a crucial skill for any Python-related job, especially in data science and machine learning."
         }
     ]

     },


       {"id": 0,
     "image": "https://media.istockphoto.com/id/1371339413/photo/co-working-team-meeting-concept-businessman-using-smart-phone-and-digital-tablet-and-laptop.webp?s=2048x2048&w=is&k=20&c=k0HGlKZDGIpAIQCx4RUEjdT-KlPoPx5iJyU6QQt9O-8=",
     "title": "How to Be a Fullstack developer in 2023 and how to learn the HTML, CSS, javaScript and one backend langauge that can be any nodeJs,PHP, python and java? ",
     "extra": "As one of the most popular programming languages out there, many people want to learn Python. But how do you go about getting started? In this guide, we explore everything you need to know to begin your learning journey, including a step-by-step guide and learning plan and some of the most useful resources to help you succeed.",
     "content1_title": "What is Python?",
     "content1": "Python is a high-level, interpreted programming language created by Guido van Rossum and first released in 1991. It is designed with an emphasis on code readability, and its syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C++ or Java.",
     "content1_": "Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming. In simpler terms, this means it’s flexible and allows you to write code in different ways, whether that's like giving the computer a to-do list (procedural), creating digital models of things or concepts (object-oriented), or treating your code like a math problem (functional).",
     "content2_title": "What makes Python so popular?",
     "content2": "As of July 2023, Python remains the most popular programing language according to the TIOBE index. Over the years, Python has become one of the most popular programming languages due to its simplicity, versatility, and wide range of applications",
     "content2image": "https://images.datacamp.com/image/upload/v1688732584/image_bcd7581290.png",
     "content2_": "These reasons also mean it is a highly favored language for data science as it allows data scientists to focus more on data interpretation rather than language complexities.",
     "content2__": "Let’s explore these factors in more..",
     "content3_title": "The main features of Python",
     "features": [
         {
              "title": "Readability.",
             "content": " Python is known for its clear and readable syntax, which resembles English to a certain extent.",
         },
         {
             "title": "Easy to learn.",
             "content": "Python’s readability makes it relatively easy for beginners to pick up the language and understand what the code is doing.",
         },
         {
             "title": "Versatility. ",
             "content": "Python is not limited to one type of task; you can use it in many fields. Whether you're interested in web development, automating tasks, or diving into data science, Python has the tools to help you get there."
         },
         {
             "title": "Rich library support.",
             "content": "It comes with a large standard library that includes pre-written code for various tasks, saving you time and effort. Additionally, Python's vibrant community has developed thousands of third-party packages, which extend Python's functionality even further."
         },

         {
             "title": "Platform independence. ",
             "content": "One of the great things about the language is that you can write your code once and run it on any operating system. This feature makes Python a great choice if you're working on a team with different operating systems."
         },

         {
             "title": "Interpreted language.",
             "content": " Python is an interpreted language, which means the code is executed line by line. This can make debugging easier because you can test small pieces of code without having to compile the whole program."
         },

         {
             "title": "Open source and free",
             "content": "It’s also an open-source language, which means its source code is freely available and can be distributed and modified. This has led to a large community of developers contributing to its development and creating a vast ecosystem of Python libraries."
         },
         {
             "title": "Dynamically typed. ",
             #  "title": "",
             "content": "Python is dynamically typed, meaning you don't have to declare the data type of a variable when you create it. The Python interpreter infers the type, which makes the code more flexible and easy to work with.",
         }

     ],

     "content4_title": "An Example Python Learning Plan",
     "content4": "Below, we’ve created a potential learning plan outlining where to focus your time and efforts if you’re just starting out with Python. Remember, the timescales, subject areas, and progress all depend on a wide range of variables. We want to make this plan as hands-on and practical as possible, which is why we’ve recommended projects you can work on as you progress.",
     "content5_title": "Month 1-3: Basics of Python and data manipulation",
     "content5": "Master basic and intermediate programming concepts. Start doing basic projects in your specialized field. For example, if you're interested in data science, you might start by analyzing a dataset using pandas and visualizing the data with matplotlib.",
     "howtolearn": [
         {
             "title": "Python basics",
             "content": "Start with the fundamentals of Python. This includes understanding the syntax, data types, control structures, functions, and more."
         },
         {
             "title": "Data manipulation",
             "content": " Learn how to handle and manipulate data using Python libraries like pandas and NumPy. This is a crucial skill for any Python-related job, especially in data science and machine learning."
         }
     ]

     },


       {"id": 0,
     "image": "https://media.istockphoto.com/id/1371339413/photo/co-working-team-meeting-concept-businessman-using-smart-phone-and-digital-tablet-and-laptop.webp?s=2048x2048&w=is&k=20&c=k0HGlKZDGIpAIQCx4RUEjdT-KlPoPx5iJyU6QQt9O-8=",
     "title": "How to Be a Fullstack developer in 2023 and how to learn the HTML, CSS, javaScript and one backend langauge that can be any nodeJs,PHP, python and java? ",
     "extra": "As one of the most popular programming languages out there, many people want to learn Python. But how do you go about getting started? In this guide, we explore everything you need to know to begin your learning journey, including a step-by-step guide and learning plan and some of the most useful resources to help you succeed.",
     "content1_title": "What is Python?",
     "content1": "Python is a high-level, interpreted programming language created by Guido van Rossum and first released in 1991. It is designed with an emphasis on code readability, and its syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C++ or Java.",
     "content1_": "Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming. In simpler terms, this means it’s flexible and allows you to write code in different ways, whether that's like giving the computer a to-do list (procedural), creating digital models of things or concepts (object-oriented), or treating your code like a math problem (functional).",
     "content2_title": "What makes Python so popular?",
     "content2": "As of July 2023, Python remains the most popular programing language according to the TIOBE index. Over the years, Python has become one of the most popular programming languages due to its simplicity, versatility, and wide range of applications",
     "content2image": "https://images.datacamp.com/image/upload/v1688732584/image_bcd7581290.png",
     "content2_": "These reasons also mean it is a highly favored language for data science as it allows data scientists to focus more on data interpretation rather than language complexities.",
     "content2__": "Let’s explore these factors in more..",
     "content3_title": "The main features of Python",
     "features": [
         {
              "title": "Readability.",
             "content": " Python is known for its clear and readable syntax, which resembles English to a certain extent.",
         },
         {
             "title": "Easy to learn.",
             "content": "Python’s readability makes it relatively easy for beginners to pick up the language and understand what the code is doing.",
         },
         {
             "title": "Versatility. ",
             "content": "Python is not limited to one type of task; you can use it in many fields. Whether you're interested in web development, automating tasks, or diving into data science, Python has the tools to help you get there."
         },
         {
             "title": "Rich library support.",
             "content": "It comes with a large standard library that includes pre-written code for various tasks, saving you time and effort. Additionally, Python's vibrant community has developed thousands of third-party packages, which extend Python's functionality even further."
         },

         {
             "title": "Platform independence. ",
             "content": "One of the great things about the language is that you can write your code once and run it on any operating system. This feature makes Python a great choice if you're working on a team with different operating systems."
         },

         {
             "title": "Interpreted language.",
             "content": " Python is an interpreted language, which means the code is executed line by line. This can make debugging easier because you can test small pieces of code without having to compile the whole program."
         },

         {
             "title": "Open source and free",
             "content": "It’s also an open-source language, which means its source code is freely available and can be distributed and modified. This has led to a large community of developers contributing to its development and creating a vast ecosystem of Python libraries."
         },
         {
             "title": "Dynamically typed. ",
             #  "title": "",
             "content": "Python is dynamically typed, meaning you don't have to declare the data type of a variable when you create it. The Python interpreter infers the type, which makes the code more flexible and easy to work with.",
         }

     ],

     "content4_title": "An Example Python Learning Plan",
     "content4": "Below, we’ve created a potential learning plan outlining where to focus your time and efforts if you’re just starting out with Python. Remember, the timescales, subject areas, and progress all depend on a wide range of variables. We want to make this plan as hands-on and practical as possible, which is why we’ve recommended projects you can work on as you progress.",
     "content5_title": "Month 1-3: Basics of Python and data manipulation",
     "content5": "Master basic and intermediate programming concepts. Start doing basic projects in your specialized field. For example, if you're interested in data science, you might start by analyzing a dataset using pandas and visualizing the data with matplotlib.",
     "howtolearn": [
         {
             "title": "Python basics",
             "content": "Start with the fundamentals of Python. This includes understanding the syntax, data types, control structures, functions, and more."
         },
         {
             "title": "Data manipulation",
             "content": " Learn how to handle and manipulate data using Python libraries like pandas and NumPy. This is a crucial skill for any Python-related job, especially in data science and machine learning."
         }
     ]

     },


       {"id": 0,
     "image": "https://media.istockphoto.com/id/1371339413/photo/co-working-team-meeting-concept-businessman-using-smart-phone-and-digital-tablet-and-laptop.webp?s=2048x2048&w=is&k=20&c=k0HGlKZDGIpAIQCx4RUEjdT-KlPoPx5iJyU6QQt9O-8=",
     "title": "How to Be a Fullstack developer in 2023 and how to learn the HTML, CSS, javaScript and one backend langauge that can be any nodeJs,PHP, python and java? ",
     "extra": "As one of the most popular programming languages out there, many people want to learn Python. But how do you go about getting started? In this guide, we explore everything you need to know to begin your learning journey, including a step-by-step guide and learning plan and some of the most useful resources to help you succeed.",
     "content1_title": "What is Python?",
     "content1": "Python is a high-level, interpreted programming language created by Guido van Rossum and first released in 1991. It is designed with an emphasis on code readability, and its syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C++ or Java.",
     "content1_": "Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming. In simpler terms, this means it’s flexible and allows you to write code in different ways, whether that's like giving the computer a to-do list (procedural), creating digital models of things or concepts (object-oriented), or treating your code like a math problem (functional).",
     "content2_title": "What makes Python so popular?",
     "content2": "As of July 2023, Python remains the most popular programing language according to the TIOBE index. Over the years, Python has become one of the most popular programming languages due to its simplicity, versatility, and wide range of applications",
     "content2image": "https://images.datacamp.com/image/upload/v1688732584/image_bcd7581290.png",
     "content2_": "These reasons also mean it is a highly favored language for data science as it allows data scientists to focus more on data interpretation rather than language complexities.",
     "content2__": "Let’s explore these factors in more..",
     "content3_title": "The main features of Python",
     "features": [
         {
              "title": "Readability.",
             "content": " Python is known for its clear and readable syntax, which resembles English to a certain extent.",
         },
         {
             "title": "Easy to learn.",
             "content": "Python’s readability makes it relatively easy for beginners to pick up the language and understand what the code is doing.",
         },
         {
             "title": "Versatility. ",
             "content": "Python is not limited to one type of task; you can use it in many fields. Whether you're interested in web development, automating tasks, or diving into data science, Python has the tools to help you get there."
         },
         {
             "title": "Rich library support.",
             "content": "It comes with a large standard library that includes pre-written code for various tasks, saving you time and effort. Additionally, Python's vibrant community has developed thousands of third-party packages, which extend Python's functionality even further."
         },

         {
             "title": "Platform independence. ",
             "content": "One of the great things about the language is that you can write your code once and run it on any operating system. This feature makes Python a great choice if you're working on a team with different operating systems."
         },

         {
             "title": "Interpreted language.",
             "content": " Python is an interpreted language, which means the code is executed line by line. This can make debugging easier because you can test small pieces of code without having to compile the whole program."
         },

         {
             "title": "Open source and free",
             "content": "It’s also an open-source language, which means its source code is freely available and can be distributed and modified. This has led to a large community of developers contributing to its development and creating a vast ecosystem of Python libraries."
         },
         {
             "title": "Dynamically typed. ",
             #  "title": "",
             "content": "Python is dynamically typed, meaning you don't have to declare the data type of a variable when you create it. The Python interpreter infers the type, which makes the code more flexible and easy to work with.",
         }

     ],

     "content4_title": "An Example Python Learning Plan",
     "content4": "Below, we’ve created a potential learning plan outlining where to focus your time and efforts if you’re just starting out with Python. Remember, the timescales, subject areas, and progress all depend on a wide range of variables. We want to make this plan as hands-on and practical as possible, which is why we’ve recommended projects you can work on as you progress.",
     "content5_title": "Month 1-3: Basics of Python and data manipulation",
     "content5": "Master basic and intermediate programming concepts. Start doing basic projects in your specialized field. For example, if you're interested in data science, you might start by analyzing a dataset using pandas and visualizing the data with matplotlib.",
     "howtolearn": [
         {
             "title": "Python basics",
             "content": "Start with the fundamentals of Python. This includes understanding the syntax, data types, control structures, functions, and more."
         },
         {
             "title": "Data manipulation",
             "content": " Learn how to handle and manipulate data using Python libraries like pandas and NumPy. This is a crucial skill for any Python-related job, especially in data science and machine learning."
         }
     ]

     },


]


new_blogs = [
           {"id": 0,
     "image": "https://media.istockphoto.com/id/1371339413/photo/co-working-team-meeting-concept-businessman-using-smart-phone-and-digital-tablet-and-laptop.webp?s=2048x2048&w=is&k=20&c=k0HGlKZDGIpAIQCx4RUEjdT-KlPoPx5iJyU6QQt9O-8=",
     "title": "How to Be a Fullstack developer in 2023 and how to learn the HTML, CSS, javaScript and one backend langauge that can be any nodeJs,PHP, python and java? ",
     "extra": "As one of the most popular programming languages out there, many people want to learn Python. But how do you go about getting started? In this guide, we explore everything you need to know to begin your learning journey, including a step-by-step guide and learning plan and some of the most useful resources to help you succeed.",
     "content1_title": "What is Python?",
     "content1": "Python is a high-level, interpreted programming language created by Guido van Rossum and first released in 1991. It is designed with an emphasis on code readability, and its syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C++ or Java.",
     "content1_": "Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming. In simpler terms, this means it’s flexible and allows you to write code in different ways, whether that's like giving the computer a to-do list (procedural), creating digital models of things or concepts (object-oriented), or treating your code like a math problem (functional).",
     "content2_title": "What makes Python so popular?",
     "content2": "As of July 2023, Python remains the most popular programing language according to the TIOBE index. Over the years, Python has become one of the most popular programming languages due to its simplicity, versatility, and wide range of applications",
     "content2image": "https://images.datacamp.com/image/upload/v1688732584/image_bcd7581290.png",
     "content2_": "These reasons also mean it is a highly favored language for data science as it allows data scientists to focus more on data interpretation rather than language complexities.",
     "content2__": "Let’s explore these factors in more..",
     "content3_title": "The main features of Python",
     "features": [
         {
              "title": "Readability.",
             "content": " Python is known for its clear and readable syntax, which resembles English to a certain extent.",
         },
         {
             "title": "Easy to learn.",
             "content": "Python’s readability makes it relatively easy for beginners to pick up the language and understand what the code is doing.",
         },
         {
             "title": "Versatility. ",
             "content": "Python is not limited to one type of task; you can use it in many fields. Whether you're interested in web development, automating tasks, or diving into data science, Python has the tools to help you get there."
         },
         {
             "title": "Rich library support.",
             "content": "It comes with a large standard library that includes pre-written code for various tasks, saving you time and effort. Additionally, Python's vibrant community has developed thousands of third-party packages, which extend Python's functionality even further."
         },

         {
             "title": "Platform independence. ",
             "content": "One of the great things about the language is that you can write your code once and run it on any operating system. This feature makes Python a great choice if you're working on a team with different operating systems."
         },

         {
             "title": "Interpreted language.",
             "content": " Python is an interpreted language, which means the code is executed line by line. This can make debugging easier because you can test small pieces of code without having to compile the whole program."
         },

         {
             "title": "Open source and free",
             "content": "It’s also an open-source language, which means its source code is freely available and can be distributed and modified. This has led to a large community of developers contributing to its development and creating a vast ecosystem of Python libraries."
         },
         {
             "title": "Dynamically typed. ",
             #  "title": "",
             "content": "Python is dynamically typed, meaning you don't have to declare the data type of a variable when you create it. The Python interpreter infers the type, which makes the code more flexible and easy to work with.",
         }

     ],

     "content4_title": "An Example Python Learning Plan",
     "content4": "Below, we’ve created a potential learning plan outlining where to focus your time and efforts if you’re just starting out with Python. Remember, the timescales, subject areas, and progress all depend on a wide range of variables. We want to make this plan as hands-on and practical as possible, which is why we’ve recommended projects you can work on as you progress.",
     "content5_title": "Month 1-3: Basics of Python and data manipulation",
     "content5": "Master basic and intermediate programming concepts. Start doing basic projects in your specialized field. For example, if you're interested in data science, you might start by analyzing a dataset using pandas and visualizing the data with matplotlib.",
     "howtolearn": [
         {
             "title": "Python basics",
             "content": "Start with the fundamentals of Python. This includes understanding the syntax, data types, control structures, functions, and more."
         },
         {
             "title": "Data manipulation",
             "content": " Learn how to handle and manipulate data using Python libraries like pandas and NumPy. This is a crucial skill for any Python-related job, especially in data science and machine learning."
         }
     ]

     },


       {"id": 0,
     "image": "https://media.istockphoto.com/id/1371339413/photo/co-working-team-meeting-concept-businessman-using-smart-phone-and-digital-tablet-and-laptop.webp?s=2048x2048&w=is&k=20&c=k0HGlKZDGIpAIQCx4RUEjdT-KlPoPx5iJyU6QQt9O-8=",
     "title": "How to Be a Fullstack developer in 2023 and how to learn the HTML, CSS, javaScript and one backend langauge that can be any nodeJs,PHP, python and java? ",
     "extra": "As one of the most popular programming languages out there, many people want to learn Python. But how do you go about getting started? In this guide, we explore everything you need to know to begin your learning journey, including a step-by-step guide and learning plan and some of the most useful resources to help you succeed.",
     "content1_title": "What is Python?",
     "content1": "Python is a high-level, interpreted programming language created by Guido van Rossum and first released in 1991. It is designed with an emphasis on code readability, and its syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C++ or Java.",
     "content1_": "Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming. In simpler terms, this means it’s flexible and allows you to write code in different ways, whether that's like giving the computer a to-do list (procedural), creating digital models of things or concepts (object-oriented), or treating your code like a math problem (functional).",
     "content2_title": "What makes Python so popular?",
     "content2": "As of July 2023, Python remains the most popular programing language according to the TIOBE index. Over the years, Python has become one of the most popular programming languages due to its simplicity, versatility, and wide range of applications",
     "content2image": "https://images.datacamp.com/image/upload/v1688732584/image_bcd7581290.png",
     "content2_": "These reasons also mean it is a highly favored language for data science as it allows data scientists to focus more on data interpretation rather than language complexities.",
     "content2__": "Let’s explore these factors in more..",
     "content3_title": "The main features of Python",
     "features": [
         {
              "title": "Readability.",
             "content": " Python is known for its clear and readable syntax, which resembles English to a certain extent.",
         },
         {
             "title": "Easy to learn.",
             "content": "Python’s readability makes it relatively easy for beginners to pick up the language and understand what the code is doing.",
         },
         {
             "title": "Versatility. ",
             "content": "Python is not limited to one type of task; you can use it in many fields. Whether you're interested in web development, automating tasks, or diving into data science, Python has the tools to help you get there."
         },
         {
             "title": "Rich library support.",
             "content": "It comes with a large standard library that includes pre-written code for various tasks, saving you time and effort. Additionally, Python's vibrant community has developed thousands of third-party packages, which extend Python's functionality even further."
         },

         {
             "title": "Platform independence. ",
             "content": "One of the great things about the language is that you can write your code once and run it on any operating system. This feature makes Python a great choice if you're working on a team with different operating systems."
         },

         {
             "title": "Interpreted language.",
             "content": " Python is an interpreted language, which means the code is executed line by line. This can make debugging easier because you can test small pieces of code without having to compile the whole program."
         },

         {
             "title": "Open source and free",
             "content": "It’s also an open-source language, which means its source code is freely available and can be distributed and modified. This has led to a large community of developers contributing to its development and creating a vast ecosystem of Python libraries."
         },
         {
             "title": "Dynamically typed. ",
             #  "title": "",
             "content": "Python is dynamically typed, meaning you don't have to declare the data type of a variable when you create it. The Python interpreter infers the type, which makes the code more flexible and easy to work with.",
         }

     ],

     "content4_title": "An Example Python Learning Plan",
     "content4": "Below, we’ve created a potential learning plan outlining where to focus your time and efforts if you’re just starting out with Python. Remember, the timescales, subject areas, and progress all depend on a wide range of variables. We want to make this plan as hands-on and practical as possible, which is why we’ve recommended projects you can work on as you progress.",
     "content5_title": "Month 1-3: Basics of Python and data manipulation",
     "content5": "Master basic and intermediate programming concepts. Start doing basic projects in your specialized field. For example, if you're interested in data science, you might start by analyzing a dataset using pandas and visualizing the data with matplotlib.",
     "howtolearn": [
         {
             "title": "Python basics",
             "content": "Start with the fundamentals of Python. This includes understanding the syntax, data types, control structures, functions, and more."
         },
         {
             "title": "Data manipulation",
             "content": " Learn how to handle and manipulate data using Python libraries like pandas and NumPy. This is a crucial skill for any Python-related job, especially in data science and machine learning."
         }
     ]

     },


       {"id": 0,
     "image": "https://media.istockphoto.com/id/1371339413/photo/co-working-team-meeting-concept-businessman-using-smart-phone-and-digital-tablet-and-laptop.webp?s=2048x2048&w=is&k=20&c=k0HGlKZDGIpAIQCx4RUEjdT-KlPoPx5iJyU6QQt9O-8=",
     "title": "How to Be a Fullstack developer in 2023 and how to learn the HTML, CSS, javaScript and one backend langauge that can be any nodeJs,PHP, python and java? ",
     "extra": "As one of the most popular programming languages out there, many people want to learn Python. But how do you go about getting started? In this guide, we explore everything you need to know to begin your learning journey, including a step-by-step guide and learning plan and some of the most useful resources to help you succeed.",
     "content1_title": "What is Python?",
     "content1": "Python is a high-level, interpreted programming language created by Guido van Rossum and first released in 1991. It is designed with an emphasis on code readability, and its syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C++ or Java.",
     "content1_": "Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming. In simpler terms, this means it’s flexible and allows you to write code in different ways, whether that's like giving the computer a to-do list (procedural), creating digital models of things or concepts (object-oriented), or treating your code like a math problem (functional).",
     "content2_title": "What makes Python so popular?",
     "content2": "As of July 2023, Python remains the most popular programing language according to the TIOBE index. Over the years, Python has become one of the most popular programming languages due to its simplicity, versatility, and wide range of applications",
     "content2image": "https://images.datacamp.com/image/upload/v1688732584/image_bcd7581290.png",
     "content2_": "These reasons also mean it is a highly favored language for data science as it allows data scientists to focus more on data interpretation rather than language complexities.",
     "content2__": "Let’s explore these factors in more..",
     "content3_title": "The main features of Python",
     "features": [
         {
              "title": "Readability.",
             "content": " Python is known for its clear and readable syntax, which resembles English to a certain extent.",
         },
         {
             "title": "Easy to learn.",
             "content": "Python’s readability makes it relatively easy for beginners to pick up the language and understand what the code is doing.",
         },
         {
             "title": "Versatility. ",
             "content": "Python is not limited to one type of task; you can use it in many fields. Whether you're interested in web development, automating tasks, or diving into data science, Python has the tools to help you get there."
         },
         {
             "title": "Rich library support.",
             "content": "It comes with a large standard library that includes pre-written code for various tasks, saving you time and effort. Additionally, Python's vibrant community has developed thousands of third-party packages, which extend Python's functionality even further."
         },

         {
             "title": "Platform independence. ",
             "content": "One of the great things about the language is that you can write your code once and run it on any operating system. This feature makes Python a great choice if you're working on a team with different operating systems."
         },

         {
             "title": "Interpreted language.",
             "content": " Python is an interpreted language, which means the code is executed line by line. This can make debugging easier because you can test small pieces of code without having to compile the whole program."
         },

         {
             "title": "Open source and free",
             "content": "It’s also an open-source language, which means its source code is freely available and can be distributed and modified. This has led to a large community of developers contributing to its development and creating a vast ecosystem of Python libraries."
         },
         {
             "title": "Dynamically typed. ",
             #  "title": "",
             "content": "Python is dynamically typed, meaning you don't have to declare the data type of a variable when you create it. The Python interpreter infers the type, which makes the code more flexible and easy to work with.",
         }

     ],

     "content4_title": "An Example Python Learning Plan",
     "content4": "Below, we’ve created a potential learning plan outlining where to focus your time and efforts if you’re just starting out with Python. Remember, the timescales, subject areas, and progress all depend on a wide range of variables. We want to make this plan as hands-on and practical as possible, which is why we’ve recommended projects you can work on as you progress.",
     "content5_title": "Month 1-3: Basics of Python and data manipulation",
     "content5": "Master basic and intermediate programming concepts. Start doing basic projects in your specialized field. For example, if you're interested in data science, you might start by analyzing a dataset using pandas and visualizing the data with matplotlib.",
     "howtolearn": [
         {
             "title": "Python basics",
             "content": "Start with the fundamentals of Python. This includes understanding the syntax, data types, control structures, functions, and more."
         },
         {
             "title": "Data manipulation",
             "content": " Learn how to handle and manipulate data using Python libraries like pandas and NumPy. This is a crucial skill for any Python-related job, especially in data science and machine learning."
         }
     ]

     },


       {"id": 0,
     "image": "https://media.istockphoto.com/id/1371339413/photo/co-working-team-meeting-concept-businessman-using-smart-phone-and-digital-tablet-and-laptop.webp?s=2048x2048&w=is&k=20&c=k0HGlKZDGIpAIQCx4RUEjdT-KlPoPx5iJyU6QQt9O-8=",
     "title": "How to Be a Fullstack developer in 2023 and how to learn the HTML, CSS, javaScript and one backend langauge that can be any nodeJs,PHP, python and java? ",
     "extra": "As one of the most popular programming languages out there, many people want to learn Python. But how do you go about getting started? In this guide, we explore everything you need to know to begin your learning journey, including a step-by-step guide and learning plan and some of the most useful resources to help you succeed.",
     "content1_title": "What is Python?",
     "content1": "Python is a high-level, interpreted programming language created by Guido van Rossum and first released in 1991. It is designed with an emphasis on code readability, and its syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C++ or Java.",
     "content1_": "Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming. In simpler terms, this means it’s flexible and allows you to write code in different ways, whether that's like giving the computer a to-do list (procedural), creating digital models of things or concepts (object-oriented), or treating your code like a math problem (functional).",
     "content2_title": "What makes Python so popular?",
     "content2": "As of July 2023, Python remains the most popular programing language according to the TIOBE index. Over the years, Python has become one of the most popular programming languages due to its simplicity, versatility, and wide range of applications",
     "content2image": "https://images.datacamp.com/image/upload/v1688732584/image_bcd7581290.png",
     "content2_": "These reasons also mean it is a highly favored language for data science as it allows data scientists to focus more on data interpretation rather than language complexities.",
     "content2__": "Let’s explore these factors in more..",
     "content3_title": "The main features of Python",
     "features": [
         {
              "title": "Readability.",
             "content": " Python is known for its clear and readable syntax, which resembles English to a certain extent.",
         },
         {
             "title": "Easy to learn.",
             "content": "Python’s readability makes it relatively easy for beginners to pick up the language and understand what the code is doing.",
         },
         {
             "title": "Versatility. ",
             "content": "Python is not limited to one type of task; you can use it in many fields. Whether you're interested in web development, automating tasks, or diving into data science, Python has the tools to help you get there."
         },
         {
             "title": "Rich library support.",
             "content": "It comes with a large standard library that includes pre-written code for various tasks, saving you time and effort. Additionally, Python's vibrant community has developed thousands of third-party packages, which extend Python's functionality even further."
         },

         {
             "title": "Platform independence. ",
             "content": "One of the great things about the language is that you can write your code once and run it on any operating system. This feature makes Python a great choice if you're working on a team with different operating systems."
         },

         {
             "title": "Interpreted language.",
             "content": " Python is an interpreted language, which means the code is executed line by line. This can make debugging easier because you can test small pieces of code without having to compile the whole program."
         },

         {
             "title": "Open source and free",
             "content": "It’s also an open-source language, which means its source code is freely available and can be distributed and modified. This has led to a large community of developers contributing to its development and creating a vast ecosystem of Python libraries."
         },
         {
             "title": "Dynamically typed. ",
             #  "title": "",
             "content": "Python is dynamically typed, meaning you don't have to declare the data type of a variable when you create it. The Python interpreter infers the type, which makes the code more flexible and easy to work with.",
         }

     ],

     "content4_title": "An Example Python Learning Plan",
     "content4": "Below, we’ve created a potential learning plan outlining where to focus your time and efforts if you’re just starting out with Python. Remember, the timescales, subject areas, and progress all depend on a wide range of variables. We want to make this plan as hands-on and practical as possible, which is why we’ve recommended projects you can work on as you progress.",
     "content5_title": "Month 1-3: Basics of Python and data manipulation",
     "content5": "Master basic and intermediate programming concepts. Start doing basic projects in your specialized field. For example, if you're interested in data science, you might start by analyzing a dataset using pandas and visualizing the data with matplotlib.",
     "howtolearn": [
         {
             "title": "Python basics",
             "content": "Start with the fundamentals of Python. This includes understanding the syntax, data types, control structures, functions, and more."
         },
         {
             "title": "Data manipulation",
             "content": " Learn how to handle and manipulate data using Python libraries like pandas and NumPy. This is a crucial skill for any Python-related job, especially in data science and machine learning."
         }
     ]

     },
]


def Home(request):
    try:
        if request.method == 'GET':
            contact_us_review = Contact_us.objects.all()
            print(contact_us_review)
            for review  in contact_us_review:
                print(review.message)
            context = {
                'reviews': contact_us_review
            }
            return render(request, 'Home.html', context)
        if request.method == "POST":
            print('Yes e')
            fullname = request.POST['fullname']
            email = request.POST['email']
            message = request.POST['message']
            contactus = Contact_us(fullName=fullname, email=email, message=message)
            context = {
                "message":'Mesage posted!'
            }
            contactus.save()
            print('saved')
            return render(request, 'Home.html' , context)

    except Exception as e:
        return HttpResponse(f"Something Wrong referesh... {e}")


def add_blogs(request):
    try:
        if (request.method == "GET"):
            return render(request, 'upload.html')
        else:
            print('Postmethod')
        print('yes')
        return render(request, 'blogs.html')
    except Exception as e:
        return HttpResponse("Error occus", e)


# For future used
def blogs(request):
    try:
        # Itemsperpage
        itemsperpage = 16
        paginator = Paginator(api_for_blogs, itemsperpage)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
       # Pass the JSON data to the template
        context = {'api_for_blogs': page}
    # Render the template with the JSON data
        return render(request, 'blogs.html', context)
    except Exception as e:
        return HttpResponse(e)


api_view(['GET'])
def blog(request, params):
    try:
    #   print('yes')
      global context
      print("yes")
      if request.method == 'GET':
          if (params == 0 or params > 0):
              all_the_comments = Comment.objects.filter(blogid=params).order_by('-post_date')  
              if(not all_the_comments):
                  all_the_comments ="No comments"
              
              context = {
                'blog': api_for_blogs[int(params)],
                "popularblogs": api_blogs_popular_only,
                "new_blogs": new_blogs,
                "allcomments": all_the_comments,
                       }
              return render(request, 'single.html', context)

          else:
              return render(request, '404.html')
      elif request.method == "POST":
          full_name = request.POST['fullname']
          email = request.POST['email']
          comment = request.POST['comment']
          if(full_name or email or comment ):
            comment_save = Comment(fullName=full_name, email=email, comment=comment, blogid=params)
            comment_save.save()
            all_the_comments = Comment.objects.filter(blogid=params).order_by('-post_date')
            context = {
                'blog': api_for_blogs[int(params)],
                "popularblogs": api_blogs_popular_only,
                "new_blogs": new_blogs,
                "allcomments": all_the_comments,
                       }
            return render(request, 'single.html', context)

          
    except Exception as e:
        return HttpResponse(e, "This is your error")




# Function to provided the popular blogs only;
api_view(['GET'])
def blog_popular(request, params):
    try:
      print("Ok you get the popular blog    ")
    #   params_ = [int(arg) for arg in params]
        # Extract the last parameter
    #   last_param = params_[-1]
    #   print(last_param)
      global context
        # print('Yes')
    #   print(type(params))
      if request.method == 'GET':
          if (params == 0 or params > 0):
              all_the_comments = Comment.objects.filter(blogid=params).order_by('-post_date')  
            #   print(all_the_comments)
              if(not all_the_comments):
                  all_the_comments ="No comments"
              
              context = {
                'blog': api_for_blogs[int(params)],
                # "popularblogs": api_blogs_popular_only,
                "new_blogs": new_blogs,
                "allcomments": all_the_comments,
                       }
            # print(context)
            #   return HttpResponse('adf')
              return render(request, 'single.html', context)

          else:
              return render(request, '404.html')
      elif request.method == "POST":
        #   print(params, "THIS IS THE PARAMAS")
          full_name = request.POST['fullname']
          email = request.POST['email']
          comment = request.POST['comment']
          if(full_name or email or comment ):
            comment_save = Comment(fullName=full_name, email=email, comment=comment, blogid=params)
            comment_save.save()
            # print('Done')
            all_the_comments = Comment.objects.filter(blogid=params).order_by('-post_date')
            context = {
                'blog': api_for_blogs[int(params)],
                "popularblogs": api_blogs_popular_only,
                "new_blogs": new_blogs,
                "allcomments": all_the_comments,
                       }
            return render(request, 'single.html', context)

          

    except Exception as e:
        return HttpResponse(e, "This is your error")



api_view(['POST'])
def handel_comments(request, params):
    try:
        print(params)
        return
        full_name = request.POST['fullname']
        email = request.POST['email']
        comment = request.POST['comment']
        if(full_name or email or comment ):
            comment_save = Comment(full_name, email, comment)
            comment_save.save()
            print('Comment saved')
    except Exception as e:
        return HttpResponse("Error",e)