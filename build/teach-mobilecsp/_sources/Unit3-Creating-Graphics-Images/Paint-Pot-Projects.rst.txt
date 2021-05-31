.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Paint Pot Projects
==================

.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
    $(document).ready(function() {
          generateFrameworkTable(EKmapping['3.04']);
          generateHovers();
      }); 
    
    </script>
    <p class="overview"><a href="https://course.mobilecsp.org/mobilecsp/unit?unit=22&amp;lesson=151" target="_blank" title="">This lesson</a> extends the app started in the 'Paint Pot Tutorial'.  Students work in pairs to complete several challenges to enhance the app, such as adding a 4th button and changing the size of the dots, and using the Camera component to replace the Canvas's background image. It reinforces the enduring understandings that programming can be used for creative expression and that collaborating (working in pairs) is an effective way to solve problems. Among other things, it reinforces the enduring understandings that the correct use iterative design and selection are important parts of computer programming. </p>
    <table border="" class="framework" id="genTable" width="100%"></table> <p>
    <!--
    &lt;table class=&quot;framework&quot;&gt;
      &lt;tbody&gt;
        &lt;!-- Table heading.  Don&#39;t change.
        &lt;tr&gt;
          &lt;th align=&quot;center&quot;&gt;CSP Framework&lt;/th&gt;
         &lt;!-- &lt;th&gt;Lesson Activities&lt;/th&gt;
        &lt;/tr&gt;
        &lt;tr class=&quot;EU&quot;&gt;
          &lt;td colspan=&quot;2&quot;&gt;&lt;img src=&quot;assets/img/creativity.png&quot; class=&quot;BI-icon&quot;&gt;
            &lt;div class=&quot;hover bi yui-wk-div&quot; data-id=&quot;CRD&quot;&gt;BI 1: Creative Development&lt;/div&gt;, 
             EU CRD-2: Developers create and innovate using an iterative design process that is user-focused, that incorporates implementation/feedback cycles, and that leaves ample room for experimentation and risk-taking.
          &lt;/td&gt;
        &lt;/tr&gt;
        &lt;tr class=&quot;LO&quot;&gt;
          &lt;td&gt;LO CRD-2.J: Identify inputs and corresponding expected outputs or behaviors that can be used to check the correctness of an algorithm or program.
            &lt;table class=&quot;hover-tip&quot;&gt;
              &lt;tbody&gt;
                &lt;tr&gt;
                  &lt;td class=&quot;ek&quot; data-id=&quot;CRD-2.J.1&quot;&gt;EK CRD-2.J.1&lt;/td&gt;
                  &lt;td class=&quot;ek&quot; data-id=&quot;CRD-2.J.2&quot;&gt;EK CRD-2.J.2&lt;/td&gt;
                  &lt;td class=&quot;ek&quot; data-id=&quot;CRD-2.J.3&quot;&gt;EK CRD-2.J.3&lt;/td&gt;
                  &lt;td class=&quot;skill skill4&quot; data-id=&quot;4.C&quot;&gt;Skill 4.C&lt;/td&gt;
                &lt;/tr&gt;           
              &lt;/tbody&gt;
            &lt;/table&gt;
          &lt;/td&gt;
         &lt;!-- &lt;td&gt;Test and modify the program until it works correctly.
          &lt;/td&gt; 
        &lt;/tr&gt;
        
    &lt;!-- &lt;tr class=&quot;LO&quot;&gt;
          &lt;td&gt;LO 1.2.4: Collaborate in the creation of computational artifacts.
            &lt;table class=&quot;hover-tip&quot;&gt;
              &lt;tbody&gt;
                &lt;tr&gt;
                  &lt;td class=&quot;ek&quot; data-id=&quot;1.2.4A&quot;&gt;EK 1.2.4A&lt;/td&gt;
                  &lt;td class=&quot;ek&quot; data-id=&quot;1.2.4C&quot;&gt;EK 1.2.4C&lt;/td&gt;
                  &lt;td class=&quot;ek&quot; data-id=&quot;1.2.4D&quot;&gt;EK 1.2.4D&lt;/td&gt;
                &lt;/tr&gt;
                &lt;tr&gt;
                  &lt;td class=&quot;ek&quot; data-id=&quot;1.2.4E&quot;&gt;EK 1.2.4E&lt;/td&gt;
                 &lt;td class=&quot;ek&quot; data-id=&quot;1.2.4F&quot;&gt;EK 1.2.4F&lt;/td&gt;
                 &lt;td class=&quot;ctp&quot; data-id=&quot;6&quot;&gt;P 6&lt;/td&gt;
                &lt;/tr&gt;
              &lt;/tbody&gt;
            &lt;/table&gt;
          &lt;/td&gt;
          &lt;td&gt;Work in pairs to solve several programming tasks.
          &lt;/td&gt;
        &lt;/tr&gt;
    
        
    &lt;!--    &lt;tr class=&quot;EU&quot;&gt;
          &lt;td colspan=&quot;2&quot;&gt;&lt;img src=&quot;assets/img/data.png&quot; class=&quot;BI-icon&quot;&gt;
            &lt;div class=&quot;hover bi yui-wk-div&quot; data-id=&quot;3&quot;&gt;BI 3: Data and Information&lt;/div&gt;, 
              EU 3.1 - People use computer programs to processs information to gain insight and knowledge.
          &lt;/td&gt;
        &lt;/tr&gt;
        &lt;tr class=&quot;LO&quot;&gt;
          &lt;td&gt;LO 3.1.2: Collaborate when processing information to gain insight and knowledge.
            &lt;table class=&quot;hover-tip&quot;&gt;
              &lt;tbody&gt;
                &lt;tr&gt;
                  &lt;td class=&quot;ek&quot; data-id=&quot;3.1.2B&quot;&gt;EK 3.1.2B&lt;/td&gt;
                  &lt;td class=&quot;ek&quot; data-id=&quot;3.1.2E&quot;&gt;EK 3.1.2E&lt;/td&gt;
                  &lt;td class=&quot;ctp&quot; data-id=&quot;6&quot;&gt;P 6&lt;/td&gt;
                &lt;/tr&gt;          
              &lt;/tbody&gt;
            &lt;/table&gt;
          &lt;/td&gt;
          &lt;td&gt;Work in pairs to discover how to use the Camera component.
          &lt;/td&gt;
        &lt;/tr&gt;
    
        &lt;tr class=&quot;EU&quot;&gt;
          &lt;td colspan=&quot;2&quot;&gt;&lt;img src=&quot;assets/img/programming.png&quot; class=&quot;BI-icon&quot;&gt;
            &lt;div class=&quot;hover bi yui-wk-div&quot; data-id=&quot;AAP&quot;&gt;BI 3: Algorithms and Programming&lt;/div&gt;, 
              EU AAP-2: The way statements are sequenced and combined in a program determines the computed result. Programs incorporate iteration and selection constructs to represent repetition and make decisions to handle varied input values.
          &lt;/td&gt;
        &lt;/tr&gt;
        &lt;tr class=&quot;LO&quot;&gt;
          &lt;td&gt;LO AAP-2.E: For relationships between two variables, expressions, or values: a. Write expressions using relational operators. b. Evaluate expressions that use relational operators.
            &lt;table class=&quot;hover-tip&quot;&gt;
              &lt;tbody&gt;
                &lt;tr&gt;
                  &lt;td class=&quot;ek&quot; data-id=&quot;AAP-2.E.2&quot;&gt;EK AAP-2.E.2&lt;/td&gt;
                  &lt;td class=&quot;skill skill2&quot; data-id=&quot;2.B&quot;&gt;Skill 2.B&lt;/td&gt;
                &lt;/tr&gt; 
              &lt;/tbody&gt;
            &lt;/table&gt;
          &lt;/td&gt;
         &lt;!-- &lt;td&gt;Develop strategies for extending the program&#39;s functionality.
          &lt;/td&gt; 
        &lt;/tr&gt; 
        
        &lt;tr class=&quot;LO&quot;&gt;
          &lt;td&gt;LO AAP-2.H: For selection: a. Write conditional statements. b. Determine the result of conditional statements.
            &lt;table class=&quot;hover-tip&quot;&gt;
              &lt;tbody&gt;
                &lt;tr&gt;
                  &lt;td class=&quot;ek&quot; data-id=&quot;AAP-2.H.2&quot;&gt;EK AAP-2.H.2&lt;/td&gt;
                  &lt;td class=&quot;ek&quot; data-id=&quot;AAP-2.H.3&quot;&gt;EK AAP-2.H.3&lt;/td&gt;
                  &lt;td class=&quot;skill skill2&quot; data-id=&quot;2.B&quot;&gt;Skill 2.B&lt;/td&gt;
                &lt;/tr&gt;             
              &lt;/tbody&gt;
            &lt;/table&gt;
          &lt;/td&gt;
    &lt;!--      &lt;td&gt;Test and modify the program until it works correctly.
          &lt;/td&gt; 
        &lt;/tr&gt;    
    
        &lt;tr class=&quot;LO&quot;&gt;
          &lt;td&gt;LO AAP-2.I: For nested selection: a. Write nested conditional statements. b. Determine the result of nested conditional statements.
            &lt;table class=&quot;hover-tip&quot;&gt;
              &lt;tbody&gt;
                &lt;tr &gt;
                  &lt;td class=&quot;ek&quot; data-id=&quot;AAP-2.I.1&quot;&gt;EK AAP-2.I.1&lt;/td&gt;
                  &lt;td class=&quot;ek&quot; data-id=&quot;AAP-2.I.2&quot;&gt;EK AAP-2.I.2&lt;/td&gt;
                  &lt;td class=&quot;skill skill2&quot; data-id=&quot;2.B&quot;&gt;Skill 2.B&lt;/td&gt;
                &lt;/tr&gt;
                
              &lt;/tbody&gt;
            &lt;/table&gt;
          &lt;/td&gt;
         &lt;!-- &lt;td&gt;Use the pair-programming approach to complete the programming tasks.
          &lt;/td&gt; 
        &lt;/tr&gt; 
        
         &lt;!-- &lt;td&gt;Use the pair-programming approach to complete the programming tasks.
          &lt;/td&gt; 
        &lt;/tr&gt; 
    &lt;!--   &lt;tr class=&quot;EU&quot;&gt;
          &lt;td colspan=&quot;2&quot;&gt;&lt;img src=&quot;assets/img/programming.png&quot; class=&quot;BI-icon&quot;&gt;
            &lt;div class=&quot;hover bi yui-wk-div&quot; data-id=&quot;5&quot;&gt;BI 5: Programming&lt;/div&gt;, 
              EU 5.4 - Programs are developed, maintained, and used by people for different purposes.
          &lt;/td&gt;
        &lt;/tr&gt;
        &lt;tr class=&quot;LO&quot;&gt;
          &lt;td&gt;LO 5.4.1: Evaluate the correctness of a program.
            &lt;table class=&quot;hover-tip&quot;&gt;
              &lt;tbody&gt;
                &lt;tr&gt;
                  &lt;td class=&quot;ek&quot; data-id=&quot;5.4.1E&quot;&gt;EK 5.4.1E&lt;/td&gt;
                  &lt;td class=&quot;ek&quot; data-id=&quot;5.4.1G&quot;&gt;EK 5.4.1G&lt;/td&gt;
                  &lt;td class=&quot;ctp&quot; data-id=&quot;4&quot;&gt;P 4&lt;/td&gt;
                &lt;/tr&gt;
              &lt;/tbody&gt;
            &lt;/table&gt;
          &lt;/td&gt;
          &lt;td&gt;Students work in pairs to identify and fix errors in their programs.
          &lt;/td&gt;
        &lt;/tr&gt;    
     
        &lt;tr class=&quot;EU&quot;&gt;
          &lt;td colspan=&quot;2&quot;&gt;&lt;img src=&quot;assets/img/programming.png&quot; class=&quot;BI-icon&quot;&gt;
            &lt;div class=&quot;hover bi yui-wk-div&quot; data-id=&quot;5&quot;&gt;BI 5: Programming&lt;/div&gt;, 
              EU 5.5 - Programming uses mathematical and logical concepts.
          &lt;/td&gt;
        &lt;/tr&gt;
        &lt;tr class=&quot;LO&quot;&gt;
          &lt;td&gt;LO 5.5.1: Employ appropriate mathematical and logical concepts in programming.
            &lt;table class=&quot;hover-tip&quot;&gt;
              &lt;tbody&gt;
                &lt;tr&gt;
                  &lt;td class=&quot;ek&quot; data-id=&quot;5.5.1D&quot;&gt;EK 5.5.1D&lt;/td&gt;
                  &lt;td class=&quot;ctp&quot; data-id=&quot;1&quot;&gt;P 1&lt;/td&gt;
                &lt;/tr&gt;
              &lt;/tbody&gt;
            &lt;/table&gt;
          &lt;/td&gt;
          &lt;td&gt;Students use simple math concepts (incrementing and decrementing a variable) and logic concepts (if/else) to enable the user to increase and decrease the size of the dots drawn by the app. 
          &lt;/td&gt;
        &lt;/tr&gt;
        
        
      &lt;/tbody&gt;
    &lt;/table&gt;
    End of Framework table. 
    -->
    </p><div class="pd yui-wk-div">
    <h3>Professional Development</h3>
    <p><b>The Student Lesson: </b> Complete the activities for 
        <a href="https://course.mobilecsp.org/mobilecsp/unit?unit=22&amp;lesson=151" target="_blank" title="">Mobile CSP Unit 3 Lesson 3.4: Paint Pot Projects</a>.
      </p>
    </div>
    <h3>Materials</h3>
    <ul>
    <li>Presentation system (LCD projector/Interactive whiteboard)</li><li>Access to computer, laptop, or Chromebook (install the Companion app on Chromebooks)</li><li>Access to mobile device with the Companion app installed or access to the emulator installed on the computer or laptop. </li><li><a href="https://docs.google.com/document/d/1s7PTuvw0fg03iEVUIW11yvHb1TzZdk6T_woT4grvQZY" target="_blank" title="">Paint Pot Projects handout</a></li>
    </ul>
    

Learning Activities
--------------------

.. raw:: html

    <p>
    <h3 id="est-length">Estimated Length: 90 minutes</h3>
    <ul>
    <li><b>Hook/Motivation (5 Minutes):</b> Have the students review and explain how the Paint Pot app was created. Discuss some ideas for enhancements. See hints and suggestions for Paint Pot Projects.</li>
    <li><b>Experiences and Explorations (30 minutes):</b> Students work in pairs on enhancements to Paint Pot; teacher answers questions. If any of the students finish early, have them begin working on their reflections. It's important that students be encouraged to be creative not only in coming up with good ideas for their apps but also in trying to solve their problems that arise during the programming task.  Students should be encouraged to discuss their work and ideas with their partner, with other students, and with the teacher. When a program doesn't work as expected, promote the idea that the student must take on the role of a detective and investigate what is causing the problem. This is what is meant by "debugging".  It's also important for students to test their work thoroughly -- it's often not enough to run the app once and conclude that it is correct.</li>
    <li><b>Rethink, Reflect and/or Revise (10 minutes):</b> In their portfolios, have the students answer the portfolio reflection questions found in the Mobile CSP lesson. Ask students about what issues they encountered while modifying the Paint Pot app? What was helpful in resolving those issues?</li>
    <li><i><b>Optional - Presentations (45 minutes):</b> On a second day, have students finish their enhancements and then share them in mini presentations.</i></li>
    </ul>
    <div class="yui-wk-div" id="accordion">
    <h3 class="ap-classroom">AP Classroom</h3>
    <div class="yui-wk-div">
    <p>The College Board's <a href="http://myap.collegeboard.org" target="_blank" title="AP Classroom Site">AP Classroom</a> provides a question bank and Topic Questions. You may create a formative assessment quiz in AP Classroom, assign the quiz (a set of questions), and then review the results in class to identify and address any student misunderstandings.The following are suggested topic questions that you could assign once students have completed this lesson.</p>
    <h4>Suggested Topic Questions:</h4>
    <ul>
    <li>Topic 3.5 Boolean Expressions</li><li>Create PT Formative Topic 3.b (Rows 2 &amp; 3) – 3 Manage Complexity with Vars<br/></li><li>Create PT Formative Topic 3.c (Row 5) – 4 Selection
    </li><li>Create PT Formative Topic 3.d (Row 6) – 2 Testing Selection
    </li>
    </ul>
    </div>
    <h3 class="assessment">Assessment Opportunities and Solutions</h3>
    <div class="yui-wk-div">
    <h4>Solutions:</h4>
    <ul>
    <li>Note: Solutions are only available to verified educators who have joined the <a href="./unit?unit=1&amp;lesson=39" target="_blank">Teaching Mobile CSP Google group/forum in Unit 1</a>.</li>
    <li><a href="https://drive.google.com/open?id=1Ew-24LbAF53XinhdssJPn4uvB6OWOfnuUxHZ6ezEYpg" target="_blank">Paint Pot Projects Solutions</a>
    </li>
    <li><a href="https://drive.google.com/open?id=1Us4_AJcI_9Xja_1lTTr6RJmI3Ko57W4Kisv7hmXv5cw" target="_blank">Quizly Solutions</a>
    </li>
    <li><a href="https://sites.google.com/a/css.edu/jrosato-cis-1001/" target="_blank">Portfolio Reflection Questions Solutions</a>
    </li>
    </ul>
    <h4>Assessment Opportunities</h4>
    <p>You can examine students’ work on the interactive exercises (by using the <a href="http://course.mobilecsp.org/mobilecsp/teacher" target="_blank" title="Mobile CSP Teacher Dashboard">Mobile CSP Teacher Dashboard</a>) and their portfolio reflection entries to assess their progress on the learning objectives. If students are able to do what is listed there, they are ready to move on to the next lesson.
        </p><ul>
    <li><i><b>Interactive Exercises:</b></i> </li><ul><li>Students should be able to initialize and increment a global variable on their own.</li><li>Students should be able to read and write program code that contains conditionals and nested if/else statements.</li></ul>
    <li><i><b>Portfolio Reflections:</b></i> </li><ul><li>Students should be able to code a selection statement in their program and accurately explain how the code segment was created as well as describe its output.</li><li>Students should be able to understand how global variables work to store program data and begin to consider the hardware necessary to have pictures persist in their apps. </li></ul>
    <li><i><b>In the Paint Pot App enhancements, look for:</b></i> </li><ul><li>Correct use of variables </li><li>Correct use of nested if/else statements and conditionals.</li></ul>
    </ul>
    </div>
    <h3 class="diff-practice">Differentiation: More Practice</h3>
    <div class="yui-wk-div">
    <p>Students should try to complete the projects without using the Solutions videos. If they get stuck, encourage them to work with their partner, a neighboring pair, etc. and then to look at the solution videos last.</p>
    </div>
    <h3 class="diff-enrich">Differentiation: Enrichment</h3>
    <div class="yui-wk-div">
    <ul>
    <li>The current app uses buttons to increment and decrement the dot size. Students can explore using other UI components such as a slider to change the dot size.</li>
    <li>Add the ability for the user to change the width of the line drawn during the Dragged event.</li>
    <li>Allow the user to create their own colors using text boxes to set the red, green, and blue values (0 to 255) and the make color block. Read the <a href="http://appinventor.mit.edu/explore/ai2/support/blocks/colors.html" target="_blank">AI2 documentation on colors</a> to learn about creating custom colors.</li>
    </ul>
    </div>
    <h3 class="tips">Teaching Tips: Program Correctness</h3>
    <div class="yui-wk-div">
    <p>Have students exchange apps and test each others in addition to their own. Students will gain insights on how others use their apps and what may need to be improved in the user interface or in the blocks so that it works for all users. Encourage them to start thinking about all possible ways a user might interact with the app - not just the way they expect them to interact.</p>
    <p>Have the students create some test cases for the app. For each test case have the students list the initial condition and/or actions along with the expected result. See the sample test cases given in the lesson for a start.
    </p></div>
    </div> <!-- accordion -->
    <div class="pd yui-wk-div">
    

Professional Development Reflection
------------------------------------

.. raw:: html

    <p>
    <p>Discuss the following questions with other teachers in your professional development program.</p>
    <ul>
    <li>How does this lesson help students toward the enduring understanding that programs can be used for creative expression  
          <div class="hover eu yui-wk-div" data-id="CRD-2">[EU CRD-2]</div> and that working in pairs is an effective way to solve programs <div class="hover eu yui-wk-div" data-id="AAP-2">[EU AAP-2]</div>?</li>
    </ul>
    <p>
    
.. mchoice:: mcsp-3-4-1
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


    
.. fillintheblank:: mcsp-3-4-2

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