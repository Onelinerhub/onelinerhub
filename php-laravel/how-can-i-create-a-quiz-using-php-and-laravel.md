# How can I create a quiz using PHP and Laravel?
// plain

Creating a quiz using PHP and Laravel is a relatively straightforward process. First, create a database to store the quiz questions and answers. Then, create a controller to handle the logic and routing for the quiz. Finally, create views to render the quiz questions and answers.

Below is an example of code to create a controller for the quiz:

```
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class QuizController extends Controller
{
    public function index()
    {
        // Retrieve all quiz questions from the database
        $questions = Question::all();
        return view('quiz', ['questions' => $questions]);
    }

    public function store(Request $request)
    {
        // Validate the user's answers
        $request->validate([
            'answer' => 'required',
        ]);

        // Retrieve the user's answers
        $answers = $request->input('answer');

        // Calculate the user's score
        $score = 0;
        foreach ($answers as $answer) {
            $question = Question::find($answer['question_id']);
            if ($question->answer == $answer['answer']) {
                $score++;
            }
        }

        // Store the user's score
        $user = Auth::user();
        $user->score = $score;
        $user->save();

        // Redirect to the results page
        return redirect()->route('quiz.results');
    }

    public function results()
    {
        // Retrieve the user's score
        $user = Auth::user();
        $score = $user->score;
        return view('results', ['score' => $score]);
    }
}
```

The code above creates a controller that handles the logic of the quiz. It retrieves all the questions from the database, validates the user's answers, calculates the user's score, and stores the score in the database. It also redirects the user to the results page where the user's score is displayed.

The code consists of four parts:

1. Retrieve all quiz questions from the database: This part of the code retrieves all the questions from the database and passes them to the view.
2. Validate the user's answers: This part of the code validates the user's answers to make sure they are valid.
3. Calculate the user's score: This part of the code iterates through the user's answers and calculates the user's score.
4. Store the user's score in the database and redirect to the results page: This part of the code stores the user's score in the database and redirects to the results page where the user's score is displayed.

## Helpful links

- [Laravel Documentation](https://laravel.com/docs/7.x)
- [PHP Documentation](https://www.php.net/docs.php)

onelinerhub: [How can I create a quiz using PHP and Laravel?](https://onelinerhub.com/php-laravel/how-can-i-create-a-quiz-using-php-and-laravel)