.. raw:: html 

   <div class="logo-header"  id="teacher-logo"  > <img class="align-center" src="../_static/Mobile_CSP_Logo_White_transparent.png" width="250px"/> </div>

Paint Pot Refactoring and Documentation
=======================================

.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
      $(document).ready(function() {
          generateFrameworkTable(EKmapping['3.05']);
          generateHovers();
      });
    
    </script>
    <p class="overview"><a href="https://runestone.academy/runestone/books/published/mobilecsp/Unit3-Creating-Graphics-Images/Paint-Pot-Refactoring-and-Procedural-Abstraction.html" target="_blank" title="">This lesson</a> modifies the app enhanced in the 'Paint Pot Projects', not to change any functionality, but to improve the code, a process called <i>refactoring</i>. In this case we will introduce the concept of a <i>programmer-defined procedure</i> that will help reduce the complexity of our code and make it easier to read and maintain. A <i>procedure</i> is a named grouping of instructions that can be used where needed in a program by invoking its name. This is known as 'calling a procedure.' This lesson reinforces the enduring understanding that procedures are useful abstractions that are used by programmers to structure and simplify programs (procedural abstraction). We will also add comments as a way of documenting the purpose of the procedure.</p>
    <table border="" class="framework" id="genTable" width="100%"></table>
    <!--   End of Framework table. -->
    <div class="pd yui-wk-div">
    <h3>Professional Development</h3>
    <p><b>The Student Lesson: </b> Complete the activities for 
        <a href="https://runestone.academy/runestone/books/published/mobilecsp/Unit3-Creating-Graphics-Images/Paint-Pot-Refactoring-and-Procedural-Abstraction.html" target="_blank" title="">Mobile CSP Unit 3 Lesson 3.5: Paint Pot Refactoring and Documentation</a>.
      </p>
    </div>
    <h3>Materials</h3>
    <ul>
    <li>Presentation system (LCD projector/Interactive whiteboard)</li><li>Access to computer, laptop, or Chromebook (install the Companion app on Chromebooks)</li><li>Access to mobile device with the Companion app installed or access to the emulator installed on the computer or laptop. </li><li><span class="yui-non">Paint Pot Refactoring <a href="https://docs.google.com/document/d/1RVO67Pd87jr1yeD6wu7_XcAdhPP0voc4VGsCtLUL_sU/edit#heading=h.o6tft5swp3bj" target="" title="">Text Version </a>or Videos</span></li><li><a href="https://en.wikipedia.org/wiki/Code_refactoring" target="_blank" title="">Wikipedia article on refactoring</a></li>
    </ul>
    

Learning Activities
--------------------

.. raw:: html

    <p>
    <h3 id="est-length">Estimated Length: 45 minutes</h3>
    <ul>
    <li><b>Hook/Motivation (5 Minutes):</b>  Here are some suggestions.
        <ul>
    <li>Show the students the lyrics of a children's song where there is a chorus like <a href="https://en.wikipedia.org/wiki/This_Old_Man#Lyrics" target="_blank">This Old Man</a> and have them point out any lines that are repeated. These can be pulled out into a procedure called chorus and called whenever needed. This is procedural abstraction.</li>
    <li>Show the students the code from a finished Paint Pot app or the template for this app. Ask them to find the duplicated code, i.e. the same blocks of code that are used in more than one event. They should identify the blocks to update the dot size label. Explain that you will learn how to create procedures, which give a name to a block of code that can then be reused in the program. You will also be adding comments to the procedure to document what it does for yourself and other programmers.</li>
    </ul>
    </li><li><b>Experiences and Explorations (20 minutes):</b> Instructors can lead students through the tutorial, can show the video (4:32), or can allow students to watch it on their own. Students can work in pairs to either update their existing app from the Paint Pot Projects lesson, or they can use the template provided in the lesson.</li>
    <li><b>Rethink, Reflect and/or Revise (20 minutes):</b>
    <ul>
    <li>Students should work on completing the self-check exercises. If time, review them as a class to ensure students are writing procedures correctly.</li>
    <li>In their portfolios, have the students answer the portfolio reflection questions found in the Mobile CSP lesson. Now that they've refactored their code, ask them how many blocks would need to change in the code if they wanted to use a slider or another UI component to display the dot size to the user? Do they think it is easier or harder with the procedure? Can students think of where they might add comments or procedures in other apps they have created?</li>
    </ul>
    </li>
    </ul>
    <div class="yui-wk-div" id="accordion">
    <h3 class="ap-classroom">AP Classroom</h3>
    <div class="yui-wk-div">
    <p>The College Board's <a href="http://myap.collegeboard.org" target="_blank" title="AP Classroom Site">AP Classroom</a> provides a question bank and Topic Questions. You may create a formative assessment quiz in AP Classroom, assign the quiz (a set of questions), and then review the results in class to identify and address any student misunderstandings.The following are suggested topic questions that you could assign once students have completed this lesson.</p>
    <p><b>Suggested Topic Questions:</b></p><br/><ul><li><span style="font-weight: normal;">Topic 1.4 Identifying and Correcting Errors <br/></span></li></ul></h4>
    </div>
    <h3 class="assessment">Assessment Opportunities and Solutions</h3>
    <div class="yui-wk-div">
    <p><b>Solutions</b> 
    <i>Note: Solutions are only available to verified educators who have joined the <a href="../Unit1-Getting-Started/PD-Joining-the-Forum.html" target="_blank">Teaching Mobile CSP Google group/forum in Unit 1</a>.</i></p>
    <ul>
    <li><a href="https://drive.google.com/open?id=0B2IG3uhfSus-Sy01ZFIwWGFTaW8" target="_blank">Paint Pot with Procedures .aia file</a>
    </li>
    <li><a href="https://drive.google.com/open?id=1Us4_AJcI_9Xja_1lTTr6RJmI3Ko57W4Kisv7hmXv5cw" target="_blank">Quizly Solutions</a>
    </li>
    <li><a href="https://sites.google.com/a/css.edu/jrosato-cis-1001/" target="_blank" title="">Portfolio Reflection Questions Solutions</a>
    </li>
    </ul>
    <p><b>Assessment Opportunities</b></p>
    <p>You can examine students’ work on the interactive exercise and their reflection portfolio entries to assess their progress on the following learning objectives. If students are able to do what is listed there, they are ready to move on to the next lesson.
        </p><ul>
    <li><i><b>Interactive Exercises:</b></i> </li>
    <li><i><b>Portfolio Reflections:</b></i>
    <br/>LO X.X.X - Students should be able to ...
          </li>
    <li><i><b>In the Paint Pot App, look for:</b></i>
    <br/>- Correct definition of a procedure
            <br/>- Correct calling of a procedure
            <br/>- Appropriate use of comments to document the procedure
          </li>
    </ul>
    </div>
    <h3 class="diff-practice">Differentiation: More Practice</h3>
    <div class="yui-wk-div">
    <p>Students can watch this <a href="https://www.youtube.com/watch?v=xWp0JxmD314" target="_blank">1-minute video</a> on defining a procedure or read more about procedures in the <a href="http://appinventor.mit.edu/explore/ai2/support/blocks/procedures.html" target="_blank">AI Documentation</a>.</p>
    </div>
    <h3 class="diff-enrich">Differentiation: Enrichment</h3>
    <div class="yui-wk-div">
    <p>Students can review previous apps to see if they should add comments or procedures anywhere else.</p>
    </div>
    </div> <!-- accordion -->
    <div class="pd yui-wk-div">
    

Professional Development Reflection
------------------------------------

.. raw:: html

    <p>
    <p>Discuss the following questions with other teachers in your professional development program.</p>
    <ul>
    <li>How does this lesson help students toward the enduring understanding that programming is facilitated by appropriate abstractions, such as procedures?</li>
    </ul>
    <p>
    
.. poll:: mcsp-3-5-1
    :option_1: Strongly Agree
    :option_2: Agree
    :option_3: Neutral
    :option_4: Disagree
    :option_5: Strongly Disagree
  
    I am confident I can teach this lesson to my students.


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. fillintheblank:: mcsp-3-5-2

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