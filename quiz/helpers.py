from .models import Question, QuizTaken
import datetime
import random
from flask import g


def create_user_quiz():
    # get all questions
    all_questions = Question.objects()

    # get only id's from the Questions and set them in the list
    all_questions_id_list = [str(x.id) for x in all_questions]
    # randomize list of id's from this
    all_questions_id_list_random = random.sample(
        all_questions_id_list, k=all_questions.count()
    )

    list_of_questions_generated_list = list()
    quiz_taken_number_of_questions_dict = {}
    # for all randomized id's get Question object and
    # store it in a list_of_questions_generated_list
    for question_id in all_questions_id_list_random:
        question = all_questions.filter(id=question_id).first()
        quiz_taken_number_of_questions_dict = {"question": question}
        list_of_questions_generated_list.append(
            quiz_taken_number_of_questions_dict
        )

    # create QuizTaken object with all available information
    quiz_taken = QuizTaken(
        user=g.user,
        list_of_questions=list_of_questions_generated_list,
        number_of_questions=all_questions.count(),
        date_started=datetime.datetime.now(),
    )
    # save it
    quiz_taken.save()

    return quiz_taken


def set_users_questions(existing_quiz):
    if existing_quiz:
        still_has_unaswered = False
        for q_answerd in existing_quiz.list_of_questions:
            if not q_answerd.chosen_answer:
                still_has_unaswered = True
                return q_answerd.question

        if not still_has_unaswered:
            existing_quiz.is_done = True
            existing_quiz.save()
            return None

        return existing_quiz.list_of_questions[0]["question"]

    quiz_taken = create_user_quiz()

    return quiz_taken.list_of_questions[0]["question"]
