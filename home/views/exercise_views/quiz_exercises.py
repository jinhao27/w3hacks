from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from main import models
import json


@login_required(login_url="http://www.w3hacks.com/login")
def quiz_exercises(request):
    topics = models.Topic.objects.all()
    quiz_exercises = models.QuizExercise.objects.all()
    specific_topic = None

    # Creating breadcrumbs
    breadcrumbs = [
        { "text": "Home", "link": "/" },
        { "text": "Exercises", "link": "/exercises/" },
        { "text": "Quiz Exercises", "link": "/exercises/quiz-exercises/" }
    ]

    if request.GET.get("topic"):
        topic = request.GET.get("topic")

        # Iterating through project exercises to find ones that are in the topic
        iterable_quiz_exercises = quiz_exercises
        quiz_exercises = []
        for quiz_exercise in iterable_quiz_exercises:
            if quiz_exercise.topic.searchable_name == topic:
                quiz_exercises.append(quiz_exercise)

        # Check to see if topic exists
        if models.Topic.objects.filter(searchable_name=topic).exists():
            # Topic object to pass into template
            specific_topic = models.Topic.objects.get(searchable_name=topic)
        else:
            return render(request, "errors/topic-does-not-exist.html")

        # Adding topic breadcrumb if exists
        breadcrumbs.append({
            "text": specific_topic.name,
            "link": None
        })

    return render(request, "home/exercises/quiz-exercises/quiz-exercises.html", context={
        "topics": topics,
        "exercises": quiz_exercises,
        "topic": specific_topic,
        "breadcrumbs": breadcrumbs
    })


@login_required(login_url="http://www.w3hacks.com/login")
def quiz_exercise(request):
    quiz_id = request.GET.get("id")
    if quiz_id:
        if models.QuizExercise.objects.filter(id=quiz_id).exists():
            quiz_exercise = models.QuizExercise.objects.get(id=quiz_id)
        else:
            return render(request, "errors/exercise-does-not-exist.html")
    else:
        return render(request, "errors/exercise-does-not-exist.html")


    # Grabbing topic for breadcrumbs
    topic = quiz_exercise.topic

    # Creating breadcrumbs
    breadcrumbs = [
        { "text": "Home", "link": "/" },
        { "text": "Exercises", "link": "/exercises/" },
        { "text": "Quiz Exercises", "link": "/exercises/quiz-exercises/" },
        { "text": topic.name, "link": "/exercises/quiz-exercises/?topic=" + topic.searchable_name },
        { "text": quiz_exercise.name, "link": None }
    ]

    return render(request, "home/exercises/quiz-exercises/quiz-exercise.html", context={
        "exercise": quiz_exercise,
        "resources": list(quiz_exercise.resources.all()),
        "breadcrumbs": breadcrumbs
    })


@login_required(login_url="http://www.w3hacks.com/login")
def take_quiz(request):
    quiz_id = request.GET.get("id")
    if quiz_id:
        if models.QuizExercise.objects.filter(id=quiz_id).exists():
            quiz_exercise = models.QuizExercise.objects.get(id=quiz_id)
        else:
            return render(request, "errors/exercise-does-not-exist.html")
    else:
        return render(request, "errors/exercise-does-not-exist.html")

    # Grabbing topic for breadcrumbs
    topic = quiz_exercise.topic

    # Creating breadcrumbs
    breadcrumbs = [
        { "text": "Home", "link": "/" },
        { "text": "Exercises", "link": "/exercises/" },
        { "text": "Quiz Exercises", "link": "/exercises/quiz-exercises/" },
        { "text": topic.name, "link": "/exercises/quiz-exercises/?topic=" + topic.searchable_name },
        { "text": quiz_exercise.name, "link": "/exercises/quiz-exercises/exercise/?id=" + quiz_exercise.id },
        { "text": "Take Quiz", "link": None }
    ]

    # Formatting questions with question and answers
    questions = []
    for question in list(quiz_exercise.questions.all()):
        questions.append({
            "question": question.question,
            "answers": question.answers
        })

    questions = json.dumps(questions)

    # Checking to see if user already took this quiz
    user_already_taken_quiz = False
    for completed_quiz_exercise in list(request.user.profile.completed_quiz_exercises.all()):
        if completed_quiz_exercise.quiz_exercise == quiz_exercise:
            user_already_taken_quiz = True


    return render(request, "home/exercises/quiz-exercises/take-quiz.html", context={
        "quiz": quiz_exercise,
        "breadcrumbs": breadcrumbs,
        "questions": questions,
        "user_already_taken_quiz": user_already_taken_quiz
    })


@login_required(login_url="http://www.w3hacks.com/login")
def quiz_results(request):
    # Grabbing quiz from query parameters
    quiz_id = request.GET.get("id")
    if quiz_id:
        if models.QuizExercise.objects.filter(id=quiz_id).exists():
            quiz_exercise = models.QuizExercise.objects.get(id=quiz_id)
        else:
            return render(request, "errors/exercise-does-not-exist.html")
    else:
        return render(request, "errors/exercise-does-not-exist.html")

    # Grabbing topic for breadcrumbs
    topic = quiz_exercise.topic

    # Creating breadcrumbs
    breadcrumbs = [
        { "text": "Home", "link": "/" },
        { "text": "Exercises", "link": "/exercises/" },
        { "text": "Quiz Exercises", "link": "/exercises/quiz-exercises/" },
        { "text": topic.name, "link": "/exercises/quiz-exercises/?topic=" + topic.searchable_name },
        { "text": quiz_exercise.name, "link": "/exercises/quiz-exercises/exercise/?id=" + quiz_exercise.id },
        { "text": "Quiz Results", "link": None }
    ]

    # Grabbing completed quiz exercise
    if models.CompletedQuizExercise.objects.filter(quiz_exercise=quiz_exercise).exists():
        for completed_exercise in models.CompletedQuizExercise.objects.filter(quiz_exercise=quiz_exercise):
            if completed_exercise in list(request.user.profile.completed_quiz_exercises.all()):
                completed_quiz_exercise = completed_exercise
    else:
        return HttpResponse("You haven't completed this quiz yet.")

    # Organizing questions and answers for easy access
    quiz_questions = list(quiz_exercise.questions.all())
    user_answers = completed_quiz_exercise.answers
    results = []
    for i in range(len(quiz_questions)):
        result = {}
        current_question = quiz_questions[i]

        result["got_this_correct"] = (current_question.answers[current_question.correct_answer_index] == user_answers[i])
        result["question"] = current_question.question
        result["answers"] = current_question.answers
        result["correct_answer"] = current_question.answers[current_question.correct_answer_index]
        result["user_answer"] = user_answers[i]

        results.append(result)

    # results = json.dumps(results)

    return render(request, "home/exercises/quiz-exercises/quiz-results.html", context={
        "quiz_exercise": quiz_exercise,
        "completed_quiz_exercise": completed_quiz_exercise,
        "breadcrumbs": breadcrumbs,
        "results": results
    })
