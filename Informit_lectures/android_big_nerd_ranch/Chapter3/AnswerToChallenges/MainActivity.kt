package com.bignerdranch.android.geoquizz

import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.Button
import android.widget.LinearLayout
import android.widget.RelativeLayout
import android.widget.Toast
//import android.widget.Toast
//import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import com.google.android.material.snackbar.Snackbar

//import androidx.core.view.ViewCompat
//import androidx.core.view.WindowInsetsCompat
import com.bignerdranch.android.geoquizz.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    //private lateinit var trueButton:Button;
    //private lateinit var falseButton:Button;
    //private lateinit var linearLayout: LinearLayout;
    private val TAG = "AWESOME_APP";
    private lateinit var binding: ActivityMainBinding;

    private val questionBank = listOf(QuestionDecorator(Question(R.string.question_australia, true)),
        QuestionDecorator(Question(R.string.question_oceans, true)),
        QuestionDecorator(Question(R.string.question_mideast, false)),
        QuestionDecorator(Question(R.string.question_africa, false)),
        QuestionDecorator(Question(R.string.question_americas, true)),
        QuestionDecorator(Question(R.string.question_asia, true))
    );
    private var currentIndex = 0;

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        //enableEdgeToEdge()
        //setContentView(R.layout.activity_main)
        binding = ActivityMainBinding.inflate(layoutInflater);
        setContentView(binding.root);
        /*ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }*/
        //linearLayout = findViewById(R.id.main_layout)
        //trueButton = findViewById(R.id.true_button);
        //falseButton = findViewById(R.id.false_button);

        binding.trueButton.setOnClickListener { view ->
        //trueButton.setOnClickListener {view:View ->
            //Do something in response to the click here
            /* We replace Toast by Snackbar
            * Toast.makeText(this, R.string.correct_toast, Toast.LENGTH_SHORT).show();
             */
            checkAnswer(true)
            updateAnswers();
        }

        binding.falseButton.setOnClickListener {view:View ->
        //falseButton.setOnClickListener {view:View ->
            //Do something in response to the click here
            /* We replace Toast by SnackBar
            * Toast.makeText(this, R.string.incorrect_toast, Toast.LENGTH_SHORT).show();
             */

            checkAnswer(false)
            updateAnswers();
        }

        binding.nextButton.setOnClickListener {view:View ->
            currentIndex = (currentIndex + 1) % questionBank.size //easy way to loop in the question bank
            displayScore()
            updateQuestion()
            updateAnswers();
        }

        binding.previousButton.setOnClickListener {view:View ->
            currentIndex = currentIndex - 1
            if (currentIndex < 0)
                currentIndex = currentIndex + questionBank.size //easy way to loop in the question bank
            updateQuestion()
            updateAnswers();
        }

        binding.questionTextView.setOnClickListener { view ->
            currentIndex = (currentIndex + 1) % questionBank.size //easy way to loop in the question bank
            updateQuestion()
        }

        updateQuestion()
    }

    private fun updateQuestion(){
        val questionResId = questionBank[currentIndex].question.textResId;
        binding.questionTextView.setText(questionResId)
        val questionMsg = getString(questionResId);//Only for logging
        Log.d(TAG, "I ask the question |${questionMsg}| which has indice: ${currentIndex}");
    }

    private fun checkAnswer(userAnswer: Boolean){
        var questionWithAnswer = questionBank[currentIndex]
        val gameAnswer = questionWithAnswer.question.answer
        Log.d(TAG, "User answer is |${userAnswer}| the correct answer is |${gameAnswer}|");
        val snackCorrectMsg = getString(R.string.correct_toast);
        val correctSnackbar = Snackbar.make(this, binding.root, snackCorrectMsg, Snackbar.LENGTH_SHORT);
        val snackIncorrectMsg = getString(R.string.incorrect_toast);
        val incorrectSnackbar = Snackbar.make(this, binding.root, snackIncorrectMsg, Snackbar.LENGTH_SHORT);

        // The question has been answered
        questionWithAnswer.beAnswered = true;
        //It is the false button so if the real answer is true we change the snackbar
        if (userAnswer != gameAnswer){
            questionWithAnswer.rightAnswer = false
            incorrectSnackbar.show()
        } else {
            questionWithAnswer.rightAnswer = true
            correctSnackbar.show()
        }
    }

    private fun updateAnswers(){
        val questionWithAnswer = questionBank[currentIndex]
        val buttonActivated = !questionWithAnswer.beAnswered
        binding.trueButton.isEnabled = buttonActivated;
        binding.falseButton.isEnabled = buttonActivated
    };

    private fun displayScore(){
        var score:Float = 0f;
        var bankSize = questionBank.size;
        if (currentIndex == 0){
            val questionAsweredList = questionBank.filter { it.beAnswered }
            if (questionAsweredList.size == bankSize) {
                val trueAnswers = questionBank.filter({ it.beAnswered && it.rightAnswer}).size.toFloat()
                score = trueAnswers / bankSize.toFloat() * 100f
                val toastStr:String = "Partie terminée le score de réponses positives est de %+.2f".format(score);
                Log.d(TAG, "On va afficher |%s|".format(toastStr))
                Toast.makeText(this, toastStr, Toast.LENGTH_LONG).show();
            }
        }
    }
}