.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Coin Flip Experiment optional
=============================

.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
    $(document).ready(function() {
          generateFrameworkTable(EKmapping['4.06']);
          generateHovers();
      });
    
    </script>
    <p class="overview"><a href="https://course.mobilecsp.org/mobilecsp/unit?unit=23&amp;lesson=68" target="_blank" title="">This lesson</a> reinforces the enduring understanding that <i>models and simulations use abstraction to generate new understanding and knowledge</i>.  In this case students will use the coin flip model in an experiment that aims to test a hypothesis about the quality of App Inventor's random-number generator.  If App Inventor's random-number generator is a good one, then if you simulate a coin flip many times and keep track of the outcomes, it should come up heads around 50% of the time.  Students will use a pre-built app to run the coin-flip experiment many times and tabulate the results. </p>
    <table border="" class="framework" id="genTable" width="100%"></table>
    <div class="pd yui-wk-div">
    <h3>Professional Development</h3>
    <p>Complete the activities for <a href="https://course.mobilecsp.org/mobilecsp/unit?unit=23&amp;lesson=68" target="_blank" title="">Mobile CSP Unit 4 Lesson 4.6: Coin Flip Experiment</a>. 
    
    </p></div>
    <h3>Materials</h3>
    <ul>
    <li>Access to computer, laptop, or Chromebook (install the Companion app on Chromebooks)</li><li>Access to mobile device with the Companion app installed or access to the emulator installed on the computer or laptop.</li><li>Paper and pencil to record observations or access to a spreadsheet</li>
    <li><a href="https://drive.google.com/open?id=1_NfNLWJxaG4qZ2Jd2x8UctDS05twn1h6p-o3XaAcRv0" target="_blank">POGIL Roles</a></li>
    <li>Pre-built Coin Flip Experiment app (<a href="https://course.mobilecsp.org/mobilecsp/assets/img/CoinFlipExperimentV1_2019QRCode.png" target="_blank" title="">QR code to download APK</a>)</li>
    <li><i>Optional</i> - <a href="http://ai2.appinventor.mit.edu/?repo=templates.appinventor.mit.edu/trincoll/csp/unit4/templates/CoinFlipExperiment/CoinFlipExperimentV1.asc" target="_blank">Source code for app</a> - If you are using the emulator, you will need to download the source code, open it in AI2, and then run the emulator to use the app.</li>
    </ul>
    

Learning Activities
--------------------

.. raw:: html

    <p>
    <h3 id="est-length">Estimated Length: 45 minutes</h3>
    <ul>
    <li><b>Hook/Motivation (5 minutes):</b> In the last lesson, students created the Coin Flip Simulation app. 
         Using Think-Pair-Share technique, ask the students to think about whether or not this was a good approximation 
         of the randomness of a coin flip and explain why or why not. Ask them how they could test whether or not it 
         was a fair coin and how they would know that. Have the class write down a hypothesis for the experiment.
      </li>
    <li><b>Experiences and Explorations (25 minutes):</b> A fair coin is one that would flip a heads 50% of the 
        time and tails the other 50%. So, the coin flips in the app should be 50% heads and 50% tails. However, we 
        would need to test this with many flips to get more accurate data. Ask them how many flips do they think 
        are needed? (Answers of 100 or less are too few. Answers above 1000 will be more accurate.) Ask them how long 
        they think it would take them to flip a coin 1,000 times by hand and then observe how long it takes them to do 
        in the app.
        <ul>
    <li><b><i>Optional</i> - Source Code Review:</b> Show the students the source code for the app. Have them 
            explain in their own words what the algorithm does. What if the experiment was based on a faulty algorithm?  
            Note that this app checks that the input into the text field is a valid number between 1 and 100 — 
            otherwise, faulty user input would be able to crash the app.
          </li>
    <li><b>Experiment Activity:</b> <b>NOTE:  This activity has been recast as a POGIL activity for 2016-17. See
            the description of the activity on the student-facing branch.</b>
            The POGIL teams will download the <i>Coin Experiment App</i> and run the experiment.  The app lets the user 
            flip a coin N times (N &lt;= 100).  
            Teams should run the experiment 10 or 20 times, generating 1000 or 2000 coin flips, and record the results in
            a table, as described in the lesson.  The format is given in the student lesson. 
            
            <p>
              NOTE: The student lesson has a link to this Google <a href="https://docs.google.com/spreadsheets/d/1pmbjF_A6Kc1-X3a5nTdsf8YNYuAOwuEt7jotG0V_XQc" target="_blank">spreadsheet</a>. 
              Each POGIL team should make their own copy and then use it to enter their data.  It will automatically calculate 
              percentages.  Here is a <a href="https://docs.google.com/spreadsheets/d/1R-Q86fC3r0y8KtACPbnzvlTItuvqlWFkQ4ADbmrga2M" target="_blank">classroom spreadsheet</a> 
              that contains the POGIL spreadsheet plus a spreadsheet that can be used to gather
              data from each of the POGIL teams. 
            </p>
    <br/><i>Note: If you are using emulators, use the link below the barcode to download the source code for the app. 
            You can then run it on your emulator from App Inventor.</i>
    </li>
    <li><b>Discussion:</b> Each group should share their results data, either on the board or through a shared 
            Google Doc. Discuss the results and whether or not the experiment's hypothesis is true: that App Inventor’s 
            random integer block is a good approximation of the process of randomly generating a 1 half the time and a 
            2 half the time. One idea for discussing the class's results as a whole might be to have the teams input
            their totals into a Google spread sheet, such as:  
            <a href="https://docs.google.com/spreadsheets/d/1_2gAzhHdXZfIZDV-8ZKoDsTWeAXnqbrFFxY9TfhRvUg" target="_blank">Experimental results spreadsheet</a>.
          </li>
    </ul>
    </li>
    <li><b>Rethink, Reflect and/or Revise (10 minutes):</b> Have students complete their portfolio reflections.</li>
    </ul>
    <div class="yui-wk-div" id="accordion">
    <h3 class="ap-classroom">AP Classroom</h3>
    <div class="yui-wk-div">
    <p>The College Board's <a href="http://myap.collegeboard.org" target="_blank" title="AP Classroom Site">AP Classroom</a> provides a question bank and Topic Questions. You may create a formative assessment quiz in AP Classroom, assign the quiz (a set of questions), and then review the results in class to identify and address any student misunderstandings.The following are suggested topic questions that you could assign once students have completed this lesson.</p>
    <h4>Suggested Topic Questions:</h4>
    <ul>
    <li>Topic 3.16 Simulations</li>
    </ul>
    </div>
    <h3 class="assessment">Assessment Opportunities</h3>
    <div class="yui-wk-div">
    <h4>Solutions:</h4>
    <ul>
    <li>Note: Solutions are only available to verified educators who have joined the <a href="./unit?unit=1&amp;lesson=39" target="_blank">Teaching Mobile CSP Google group/forum in Unit 1</a>.</li>
    <li><a href="https://drive.google.com/open?id=1Us4_AJcI_9Xja_1lTTr6RJmI3Ko57W4Kisv7hmXv5cw" target="_blank">Quizly Solutions</a>
    </li>
    <li><a href="https://sites.google.com/a/css.edu/jrosato-cis-1001/" target="_blank">Portfolio Reflection Questions Solutions</a>
    </li>
    </ul>
    <h4>Assessment Opportunities</h4>
    <p>You can examine students’ work on the interactive exercise and their reflection portfolio entries to assess their progress on the following learning objectives. If students are able to do what is listed there, they are ready to move on to the next lesson.</p>
    <ul>
    <li><i><b>Interactive Exercises:</b></i> </li>
    <li><i><b>Portfolio Reflections:</b></i>
    <br/>LO X.X.X - Students should be able to ...
          </li>
    <li><i><b>In the XXX App, look for:</b></i>
    </li>
    </ul>
    </div>
    <h3 class="diff-enrich">Differentiation: Enrichment</h3>
    <div class="yui-wk-div">
    <p>If they haven't already, students should review the source code and explain in their own words what it does. Then, have students re-write the ButtonGo.Click algorithm in pseudocode, pointing out where selection and repetition structures are used.
      </p></div>
    <h3 class="bk-knowledge">Background Knowledge: Pseudorandomness</h3>
    <div class="yui-wk-div">
    <p>Even if you don't use the pseduorandom numbers lesson in class, the background presentation on <a href="https://www.youtube.com/watch?v=ufiFEubOSd0" target="_blank">how pseudorandom number generators</a> (PRNG's) work would be helpful to review.</p>
    </div>
    </div> <!-- accordion -->
    <div class="pd yui-wk-div">
    

Professional Development Reflection
------------------------------------

.. raw:: html

    <p>
    <p>Discuss the following questions with other teachers in your professional development program.</p>
    <ul>
    <li> How does this lesson help students toward the enduring understanding AAP-3?</li>
    </ul>
    <p>
    
.. mchoice:: mcsp-4-6-1
    :random:
    :practice: T
    :answer_a: Strongly Agree
    :feedback_a: 
    :answer_b: Agree
    :feedback_b: 
    :answer_c: Neutral
    :feedback_c: 
    :answer_d: Disagree
    :feedback_d: 
    :answer_e: Strongly Disagree
    :feedback_e: 
    :correct: a,b,c,d,e

    I am confident I can teach this lesson to my students.


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. fillintheblank:: mcsp-4-6-2

    What questions do you still have about the lesson or the content presented? |blank|

    - :/.*/i: Thank you. We will review these to improve the course.
      :x: Thank you. We will review these to improve the course.


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    </p>
    </div>
    </div>