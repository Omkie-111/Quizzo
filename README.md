# Quiz API Documentation

This repository contains an API for managing quizzes. It provides several views for creating quizzes, retrieving quiz results, and getting lists of active and all quizzes.

## API Views

The Quiz API includes the following views:

- `QuizList`: API view to create quizzes.
- `ActiveQuiz`: API view to get the list of active quizzes.
- `QuizResult`: API view to retrieve the result of a quiz.
- `AllQuizzes`: API view to get the list of all quizzes.
- `QuizCachedView`: API view with caching implemented.

### `QuizList`

This view allows creating quizzes.

**Endpoint**: `POST /quizzes/`

#### Request

The request should include the following parameters:

- `title` (string): The title of the quiz.
- `questions` (list): A list of question objects. Each question object should include:
  - `text` (string): The text of the question.
  - `choices` (list): A list of choices for the question.
  - `answer` (integer): The index of the correct answer.
 
  
Example request body:

```json
{
  "title": "My Quiz",
  "questions": [
    {
      "text": "What is 2 + 2?",
      "choices": ["3", "4", "5"],
      "answer": 1
    },
    {
      "text": "Who painted the Mona Lisa?",
      "choices": ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso"],
      "answer": 0
    }
  ]
}

#### Response

If the quiz is successfully created, the response will include the created quiz object with a status code of 201 (Created).

### `ActiveQuiz`

This view returns the list of active quizzes.

**Endpoint**: `GET /quizzes/active/`

#### Response

The response will include a list of active quizzes with a status code of 200 (OK).

### `QuizResult`

This view retrieves the result of a quiz by its ID.

**Endpoint**: `GET /quizzes/{id}/result/`

#### Response

If the quiz exists and its status is "finished," the response will include the result of the quiz. The result will be a JSON object with the `rightAnswer` field indicating the correct answer.

If the quiz doesn't exist or is not finished, the response will have a status code of 404 (Not Found).

### `AllQuizzes`

This view returns the list of all quizzes.

**Endpoint**: `GET /quizzes/all/`

#### Response

The response will include a list of all quizzes with a status code of 200 (OK).

### `QuizCachedView`

This view is an API view with caching implemented.

**Endpoint**: `GET /quizzes/cached/`

#### Response

The response will always be "OK" with a status code of 200 (OK). The response is cached for 60 seconds to improve performance.

## Conclusion

This repository provides an API for managing quizzes. Refer to the API views documentation for detailed information on how to interact with the API.

---
