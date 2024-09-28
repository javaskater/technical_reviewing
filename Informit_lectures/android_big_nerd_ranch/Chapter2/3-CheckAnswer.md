# p 43 and 44 it proposes
* *updateQuestion*
* *checkAnswer*
```kotlin
    private fun updateQuestion(){
        val questionResId = questionBank[currentIndex].textResId;
        binding.questionTextView.setText(questionResId)
        val questionMsg = getString(questionResId);//Only for logging
        Log.d(TAG, "I ask the question |${questionMsg}| which has indice: ${currentIndex}");
    }

    private fun checkAnswer(userAnswer: Boolean){
        val gameAnswer = questionBank[currentIndex].answer
        Log.d(TAG, "User answer is |${userAnswer}| the correct answer is |${gameAnswer}|");
        val snackCorrectMsg = getString(R.string.correct_toast);
        val correctSnackbar = Snackbar.make(this, binding.root, snackCorrectMsg, Snackbar.LENGTH_SHORT);
        val snackIncorrectMsg = getString(R.string.incorrect_toast);
        val incorrectSnackbar = Snackbar.make(this, binding.root, snackIncorrectMsg, Snackbar.LENGTH_SHORT);

        //It is the false button so if the real answer is true we change the snackbar
        if (userAnswer != gameAnswer){
            incorrectSnackbar.show()
        } else {
            correctSnackbar.show()
        }
    }
``` 