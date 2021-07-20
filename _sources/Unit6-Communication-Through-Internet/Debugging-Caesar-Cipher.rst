.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Debugging Caesar Cipher
=======================

.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
     $(document).ready(function() {
          generateFrameworkTable(EKmapping['6.08']);
          generateHovers();
      });
    
    </script>
    <p class="overview"><a href="../mobilecsp/unit?unit=25&amp;lesson=189" target="_blank" title="">This lesson</a> reviews debugging and has students debug a Caesar Cipher app with 5 bugs in it. The lesson reinforces their understanding of what it means for a program to work correctly.</p>
    <table border="" class="framework" id="genTable" width="100%"></table>
    <div class="pd yui-wk-div">
    <h3>Professional Development</h3>
    <p><b>The Student Lesson:</b> Complete the activities for <a href="../mobilecsp/unit?unit=25&amp;lesson=189" target="_blank" title="">Mobile CSP Unit 6: Lesson 6.8 Debugging Caesar App</a>.
      </p>
    </div>
    <h3>Materials</h3>
    <ul>
    <li><a href="https://docs.google.com/presentation/d/1VJzIXEueLY5EmGm5VPpKEJg07P3xxYJfa5rTwGTnVGA/edit?usp=sharing" target="_blank">Slides on Debugging</a></li>
    <li>Projection system and computer lab</li>
    <li>Devices, emulators, or Chromebooks</li>
    </ul>
    

Learning Activities
--------------------

.. raw:: html

    <p>
    <h3 id="est-length">Estimated Length: 45 minutes</h3>
    <ul>
    <li><b>Hook/Motivation (10 minutes):</b> (Think-Pair-Share) Show a sample of App Inventor code to students and ask them to write down what they think the code is supposed to do and what it actually does. Have them share answers with a partner and with the class. The example below is from a Space Invaders game with a Sprite for one of the invaders, which moves similar to the lightbulb in the Lights Off app. The MyCanvas property should be Width instead of BackgroundImage. For this example, make sure everyone in the class knows what happens in the Space Invaders game.<br/>
    <a href="assets/img/spaceinvadersUI.png" target="_blank"><img class="yui-img" height="350" src="../_static/assets/img/spaceinvadersUI.png"/></a>
    <a href="assets/img/spaceinvadersCode.png" target="_blank"><img class="yui-img" src="../_static/assets/img/spaceinvadersCode.png" width="650"/></a>
    </li>
    <li><b>Experiences and Explorations (25 minutes):</b>
    <ul>
    <li><b>Explanation (10 minutes):</b> Either use the slides to present concepts on debugging or have students watch the video.</li>
    <li><b>Debugging (15 minutes):</b> Have students download the buggy app and try to find the 5 errors. The students should do any necessary tests to determine what the bugs may be.  The students should make incremental corrections. After attempting to fix one bug, the students should test the app before continuing. If they need hints, tell them to first look at encryption, then decryption, tell them to pay attention to how many times each loop is run in these functions and their return values. They can also compare their code to their finished Caesar app from the last lesson.
            <br/>Here are the <a href="https://docs.google.com/document/d/1ICCkNgq7fA40rZrWSXOWahZpCVIqR7nPAc0YnvhBe38/edit?usp=sharing" target="_blank"><b>solutions</b></a> to this debugging exercise.</li>
    </ul>
    </li>
    <li><b>Rethink, Reflect and/or Revise (10 minutes):</b> Review the debugging strategies and syntax vs. semantic errors. Have students complete the interactive exercises and portfolio reflection</li>
    </ul>
    <div id="accordion">
    <h3 class="ap-classroom">AP Classroom</h3>
    <div class="yui-wk-div">
    <p>The College Board's <a href="http://myap.collegeboard.org" target="_blank" title="AP Classroom Site">AP Classroom</a> provides a question bank and Topic Questions. You may create a formative assessment quiz in AP Classroom, assign the quiz (a set of questions), and then review the results in class to identify and address any student misunderstandings.The following are suggested topic questions that you could assign once students have completed this lesson.</p>
    <p><b>Suggested Topic Questions:</b></p>
    </div>
    <h3 class="assessment">Assessment Opportunities and Solutions</h3>
    <div>
    <p><b>Solutions:</b></p>
    <ol>
    <li><a href="https://drive.google.com/open?id=1ICCkNgq7fA40rZrWSXOWahZpCVIqR7nPAc0YnvhBe38" target="_blank">Debugging Caesar Cipher Solutions</a></li>
    </ol>
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
    <h3 class="diff-practice">Differentiation: More Practice</h3>
    <div>
    <p>If students are struggling with the lessons, they should explain in their own words how the app is supposed to work and identify what is not working. If needed, they can review the code from the completed  app and compare it to the buggy app.</p>
    </div>
    <h3 class="diff-enrich">Differentiation: Enrichment</h3>
    <div>
    <p>Students can introduce their own bug to the app and then have a partner try to debug it.</p>
    </div>
    <h3 class="tips">Teaching Tips: Debugging</h3>
    <div>
    <p>Debugging is a very common programming practice that should be emphasized throughout the course. However, in order for students to be effective debuggers, they must first understand how the program is supposed to work. If they are struggling, have them describe out loud how the program should work and then identify what is not working correctly.</p>
    </div>
    </div> <!-- accordion -->
    <div class="pd yui-wk-div">
    

Professional Development Reflection
------------------------------------

.. raw:: html

    <p>
    <p>Discuss the following questions with other teachers in your professional development program.</p>
    <ul>
    <li><div class="hover eu yui-wk-div" data-id=""></div></li> <!-- for an EU -->
    </ul>
    <!-- These are the PD exit slips.  We should have corresponding exit slips for use after the classroom lesson. -->
    
.. mchoice:: mcsp-6-8-1
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


    
.. fillintheblank:: mcsp-6-8-2

    What questions do you still have about the lesson or the content presented? |blank|

    - :/.*/i: Thank you. We will review these to improve the course.
      :x: Thank you. We will review these to improve the course. 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    </div>
    </div>