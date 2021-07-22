.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Hardware Abstractions Logic Gates
=================================

.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
      $(document).ready(function() {
          generateFrameworkTable(EKmapping['2.10']);
          generateHovers();
      }); 
    
    </script>
    <!-- This is the overview paragraph.  The link URL should be to the corresponding lesson on the student branch. -->
    <p class="overview">
    <a href="https://course.mobilecsp.org/mobilecsp/unit?unit=1&amp;lesson=156" target="_blank" title="">This lesson </a> provides a second look at computer hardware and software. It drills deeper into the various abstraction levels that make up computer systems.  On the hardware side students are introduced to low-level examples such as gates and flip-flops.  Students see that at the very lowest level computer circuits are made up of logical elements that obey Boolean logic.  On the software side students are introduced to the distinction between high-level languages, such as App Inventor and Python, and low-level machine language, which is based on the binary system (0s and 1s). This lesson reinforces the enduring understanding that multiple levels of abstraction are used in both hardware and software. 
    </p>
    <!-- This is the framework table, where we describe how this lesson fits into the CSP framework.  -->
    <table border="" class="framework" id="genTable" width="100%"></table>
    <!--   End of Framework table. -->
    <!-- This div associates the teach branch with the corresponding student branch. It should go after the table. -->
    <div class="pd yui-wk-div">
    <h3>Professional Development</h3>
    <p><b>The Student Lesson: </b> Complete the activities for 
        <a href="https://course.mobilecsp.org/mobilecsp/unit?unit=1&amp;lesson=156" target="_blank" title="">Mobile CSP Unit 2 Lesson 2.10: Hardware and Software Abstractions</a>.
      </p>
    </div>
    <h3>Materials</h3><p></p><ul><li>Projection system</li><li>Access to computer, laptop, or Chromebook (install the Companion app on Chromebooks)</li><li><a href="https://docs.google.com/presentation/d/1yHx42yEaUzLurEuBOzQWvb0KS3oBsM7xhDh2lETod3M/" target="_blank" title="">Slides</a><br/></li><li>Access to <a href="http://logic.ly/lessons/" target="_blank">Logicly</a></li><li><a href="https://drive.google.com/open?id=1_NfNLWJxaG4qZ2Jd2x8UctDS05twn1h6p-o3XaAcRv0" target="_blank">POGIL Role Cards</a><br/></li></ul><p></p>
    

Learning Activities
--------------------

.. raw:: html

    <p>
    <h3 id="est-length">Estimated Length: 45 minutes</h3>
    <h4>Hook/Motivation (5 minutes):</h4> 
    Here are some options:
    <ul>
    <li>Ask students what's inside a computer chip? They may say circuits or wires. See if they know what a transistor is, a tiny switch controlling the flow of electricity. The invention of transistors won the Nobel prize in 1956 and have changed the world! Show the first minute of this   <a href="https://www.youtube.com/watch?v=IcrBqCFLHIY" target="_blank">video about transistors</a>, and/or this <a href="https://www.youtube.com/watch?v=Knd-U-avG0c" target="_blank">video zooming into a chip</a>. Transistors are used to make logic gates that can store information and make decisions inside a computer. </li>
    <li>
    <p>Ask students if they have learned about Boolean logic in their math courses. If so, have 
    them share what they know about the AND, OR, and NOT logical operators. Share an example relevant
    to the students. For example, you could say that two inputs to whether or not you can see a movie
    this evening could be: 1) Having $20 in their pocket and 2) Spiderman is playing at 7 pm. If 
    both of those conditions are true, then the output (result) is that they can go to the movie. If only one
    or neither of them are true, then the output is that they can't go to the movie.</p>
    <p>Draw a truth table such as the following to explain AND, OR, and NOT briefly.</p>
    <table border="1" padding="5px">
    <tbody><tr>
    <th width="35%">AND</th><th width="35%">OR</th><th width="30%">NOT</th>
    </tr>
    <tr><td>
    <table border="1">
    <tbody>
    <tr><td>Input A</td><td>Input B</td><td>Output Z</td></tr>
    <tr><td>F</td><td>F</td><td>F</td></tr>
    <tr><td>F</td><td>T</td><td>F</td></tr>
    <tr><td>T</td><td>F</td><td>F</td></tr>
    <tr><td>T</td><td>T</td><td>T</td></tr>
    </tbody></table>
    </td>
    <td>
    <table border="1">
    <tbody>
    <tr><td>Input A</td><td>Input B</td><td>Output Z</td></tr>
    <tr><td>F</td><td>F</td><td>F</td></tr>
    <tr><td>F</td><td>T</td><td>T</td></tr>
    <tr><td>T</td><td>F</td><td>T</td></tr>
    <tr><td>T</td><td>T</td><td>T</td></tr>
    </tbody></table>
    </td>
    <td valign="top" padding="2px">
    <table border="1">
    <tbody>
    <tr><td>Input</td><td>Output</td></tr>
    <tr><td>T</td><td>F</td></tr>
    <tr><td>F</td><td>T</td></tr>
    </tbody></table>
    </td>
    </tr>
    </tbody></table>
    </li></ul>
    <h4>Experiences and Explorations (30 minutes):</h4>
    <ul>
    <li><b>Lecture:</b> Topic: Hardware and Software Abstractions (<a href="https://docs.google.com/presentation/d/1yHx42yEaUzLurEuBOzQWvb0KS3oBsM7xhDh2lETod3M/" target="_blank" title="">Slides</a>) Use this presentation to give examples of varying levels of abstractions in hardware, including logic gates and flip-flops.</li>
    <li><b>Logicly Activity:</b> Break students into POGIL teams and have them explore logic gates using <a href="http://logic.ly/lessons/" target="_blank">Logicly</a>. In Logicly, the push button (or toggle) represents the input (true or false) and the light bulb represents the output. The output is true if the lightbulb is lit up (blue). Go through the live example of the <a href="https://logic.ly/lessons/and-gate/" target="_blank">AND gate</a> with your class (If you don't see the Live Example, click on the Adobe Flash link and enable Flash). Go to <a href="https://logic.ly/demo/" target="_blank">Logicly Edit mode</a> to create your own circuits.  A simple example to demonstrate how Logicly works would be to create a circuit with a toggle switch and a light bulb. As the switch is toggled from true to false, the light bulb should change whether or not it's lit up. Try adding a NOT gate between the toggle and the light bulb and show how that changes the output. (Read more about Logicly components <a href="http://logic.ly/help/components.html" target="_blank">here</a>.) They can create more complex designs (including using flip flops) and test them against an appropriate truth table. </li>
    </ul>
    <h4>See solutions to POGIL Activity in the Assessment and Solutions section below.</h4>
    <h4>Rethink, Reflect and/or Revise (10 minutes):</h4>
    <ul>
    <li>Review the answers to the POGIL prompts with the class, asking the spokesperson to report out for each group</li>
    <li>Ask the students to complete the interactive exercises on the Mobile CSP lesson</li>
    <li>Have the students complete their portfolio reflection</li>
    </ul>
    <div class="yui-wk-div" id="accordion">
    <h3 class="ap-classroom">AP Classroom</h3>
    <div class="yui-wk-div">
    <p>The College Board's <a href="http://myap.collegeboard.org" target="_blank" title="AP Classroom Site">AP Classroom</a> provides a question bank and Topic Questions. You may create a formative assessment quiz in AP Classroom, assign the quiz (a set of questions), and then review the results in class to identify and address any student misunderstandings.The following are suggested topic questions that you could assign once students have completed this lesson.</p>
    <p><b>Suggested Topic Questions:<span style="font-weight: normal;"> None</span></b></p>
    </div>
    <h3 class="assessment">Assessment Opportunities and Solutions</h3>
    <div class="yui-wk-div">
    <p><b>Solutions:</b></p>
    <ul>
    <li>Note: Solutions are only available to verified educators who have joined the <a href="./unit?unit=1&amp;lesson=39" target="_blank">Teaching Mobile CSP Google group/forum in Unit 1</a>.</li>
    <li><a href="https://drive.google.com/open?id=1Us4_AJcI_9Xja_1lTTr6RJmI3Ko57W4Kisv7hmXv5cw" target="_blank">Quizly Solutions</a>
    </li>
    <li><a href="https://docs.google.com/document/d/1fktruAhWy7vdLBmz5WUnc6bWJSJ1N-hYGhVufKyWkc0/edit?usp=sharing" target="_blank">Logic Gates POGIL Solutions</a>
    </li>
    <li><a href="https://sites.google.com/a/css.edu/jrosato-cis-1001/" target="_blank">Portfolio Reflection Questions Solutions</a>
    </li>
    </ul>
    <p><b>Assessment Opportunities</b></p>
    <p>You can examine students’ work on the interactive exercise and their reflection portfolio entries to assess their progress on the following learning objectives. If students are able to do what is listed there, they are ready to move on to the next lesson.
        </p><ul>
    <li><i><b>Interactive Exercises:</b></i> </li>
    <li><i><b>Portfolio Reflections:</b></i>
    </li>
    </ul>
    </div>
    <h3 class="diff-practice">Differentiation: More Practice</h3>
    <div class="yui-wk-div">
    <p>How Stuff Works has a series on <i><a href="http://computer.howstuffworks.com/boolean.htm" target="_blank">How Boolean Logic Works</a></i> that includes information on flip-flops and gates.</p>
    </div>
    <h3 class="diff-enrich">Differentiation: Enrichment</h3>
    <div class="yui-wk-div">
    <p>Students can build more complex circuits with Logicly. For example, a 2 bit (or 4 bit!) ripple counter using D flip flops (Q’ is connected to D and the next clock input, push the button to start the counter): <br/><img src="../_static/assets/img/ripplecounter.png" width="50%"/>
    </p><p>Have students read <a href="http://searchstorage.techtarget.com.au/news/2240019270/Solid-State-Disks-The-details" target="_blank">this article</a> explaining how SSDs (solid state drives) are composed of NAND or NOR logic gates. You might want to follow it up with portions of <a href="http://www.youtube.com/watch?v=TFoOyPXYJ-E" target="_blank">this video</a> that explains how SSDs work, especially the first part (up to 4:30).</p>
    </div>
    <h3 class="bk-knowledge">Background Knowledge: Boolean Logic</h3>
    <div class="yui-wk-div">
    <ul>
    <li>How Stuff Works has a series on <i><a href="http://computer.howstuffworks.com/boolean.htm" target="_blank">How Boolean Logic Works</a></i> that includes information on flip-flops and gates.</li>
    <li>WhatIs.com also has a glossary of terms related to computing and technology, including entries on 
           <a href="http://whatis.techtarget.com/definition/flip-flops-bistable-gates" target="_blank">flip-flops</a>,
           <a href="http://whatis.techtarget.com/definition/logic-gate-AND-OR-XOR-NOT-NAND-NOR-and-XNOR" target="_blank">logic gates</a>, and
           <a href="http://whatis.techtarget.com/definition/machine-code-machine-language" target="_blank">machine language</a>.
        </li>
    </ul>
    </div>
    </div> <!-- accordion -->
    <div class="pd yui-wk-div">
    

Professional Development Reflection
------------------------------------

.. raw:: html

    <p>
    <p>Discuss the following questions with other teachers in your professional development program.</p>
    <ul>
    <li>This lesson dives deeper into the basic components of computers and how they operate, the foundation for understanding other logic components and programming concepts.  How does this lesson help students toward the enduring understanding that computer systems are built up through several layers of abstractions? </li>
    </ul>
    <!-- These are the PD exit slips.  We should have corresponding exit slips for use after the classroom lesson. -->
    <p>
    
.. poll:: mcsp-2-10-1
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


    
.. fillintheblank:: mcsp-2-10-2

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