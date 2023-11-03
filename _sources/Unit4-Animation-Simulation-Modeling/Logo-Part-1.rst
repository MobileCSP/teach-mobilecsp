.. raw:: html 

   <div class="logo-header"  id="teacher-logo"  > <img class="align-center" src="../_static/Mobile_CSP_Logo_White_transparent.png" width="250px"/> </div>

Logo Part 1
===========

.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
     $(document).ready(function() {
          generateFrameworkTable(EKmapping['4.04']);
          generateHovers();
      });
    
    </script>
    <p class="overview"><a href="https://runestone.academy/runestone/books/published/mobilecsp/Unit4-Animation-Simulation-Modeling/Logo-Part-I.html" target="_blank" title="">This lesson</a> reinforces the use of procedures as abstraction in programming, but introduces how procedures can help reduce the complexity of algorithms. Students use an app based on the Logo programming environment that has pre-defined procedures to move a turtle around the screen and draw lines. Through a series of drawing exercises, students will be encouraged to use procedures to define each exercise, or parts of an exercise.</p>
    <table border="" class="framework" id="genTable" width="100%"></table>
    <div class="pd yui-wk-div">
    <h3>Professional Development</h3>
    <p><b>The Student Lesson:</b> Complete the activities for 
        <a href="https://runestone.academy/runestone/books/published/mobilecsp/Unit4-Animation-Simulation-Modeling/Logo-Part-I.html" target="_blank" title="">Mobile CSP Unit 4 Lesson 4.4: Logo Part 1</a>.
      </p>
    </div>
    <h3>Materials</h3>
    <ul>
    <li>Presentation system (LCD projector/Interactive whiteboard)</li><li>Access to computer, laptop, or Chromebook (install the Companion app on Chromebooks)</li><li>Access to mobile device with the Companion app installed or access to the emulator installed on the computer or laptop. </li><li>Logo Part 1 Tutorial (Video, Full Text Version, or <a href="https://docs.google.com/document/d/1McHT42xH7YT-_rV-Cu3a7l8LYGTM-Fr3NyVxI-wIX8o/edit?usp=sharing" target="_blank">short handout</a>)</li>
    <li>Graphing paper - You can print graph paper from <a href="http://www.printablepaper.net/">www.printablepaper.net</a></li>
    </ul>
    

Learning Activities
--------------------

.. raw:: html

    <p>
    <h3 id="est-length">Estimated Length: 90 minutes</h3>
    <ul>
    <li><b>Hook/Motivation (5 minutes):</b> Ask students to think about what basic commands are needed to have the "turtle" draw a square in <a href="http://youtu.be/KeFhFPNO8hc" target="_blank">this historical turtle video</a>  or modern <a href="https://www.youtube.com/watch?v=cYIZeS63c8o" target="_blank"> Lego EV3 video</a>. (Most likely they will come up with forward and turn.) Ask them to brainstorm other shapes that could be drawn using those commands.</li>
    <li><b>Experiences and Explorations (30 minutes):</b>
    <ul>
    <li><b>Explanation (5 minutes):</b> Introduce the <a href="http://en.wikipedia.org/wiki/Logo_programming_language" target="_blank">Logo environment</a> in App Inventor and explain the primitive operations. The primitive operations are the basic commands that the Android understands before being taught new commands (by defining procedures).  <i>Note: The original Logo uses a turtle. In our App Inventor version of Logo, an Android is used.</i>
    <ul>
    <li><i>forward </i>- moves the Android forward by 10 pixels. </li>
    <li><i>turn </i>- causes the Android to turn right by 90 degrees. </li>
    <li><i>setPenUp(True)</i> - pulls the pen off the canvas so nothing is drawn when the Android moves. </li>
    <li><i>setPenUp(False)</i> - puts the down on the canvas so it will draw. </li>
    <li><i>setTurtle(True)</i> - makes the Android visible. </li>
    <li><i>setTurtle(False)</i> - makes the Android invisible.</li>
    <li><span style="font-style: italic;">draw</span> - moves the Android according to the code you specify. Here is where you will put your algorithms.</li>
    <li><span style="font-style: italic;">reset</span> - clears the canvas and moves the Android back to it’s starting position.</li>
    </ul>
    </li>
    <li><b>Algorithm Practice (10 minutes):</b> Have the students create and write down an algorithm (i.e. how would they use forward and turn) to draw a 10 x 10 square and then display one of their algorithms on the board. Discuss how this is an algorithm. (See note in Background Knowledge about algorithms vs. recipes.)</li>
    <li><b>Programming Tutorial (20 minutes):</b>  Use the video or text tutorials or lead your students to do the first drawSquare exercise. Then have students work in pair programming (taking turns being on 1 computer) or buddy programming (on two computers but making sure they solve it together) to complete the rest of the exercises on their own.<p> Note that the primitives in this tutorial (forward, turn) are made deliberately weak in the hopes that students will experience some frustration that will lead them to propose something like adding <b><i>parameters</i></b> to the procedures. For example, to draw a 30 x 30 square would require the following steps (where F stands for forward and T stands for turn):
           <br/>     F F F T F F F T F F F T F F F T
           <br/>However, as they will see in the next lesson, if we use parameters, where forward becomes forward(N) so that you can say forward(30) or forward(100) to move the Android forward by a specified distance, then the algorithm for a 30 x 30 square becomes:
           <br/>     F(30)  T  F(30)  T  F(30)  T  F(30)  T</p></li>
    </ul>
    </li>
    <li><b>Rethink, Reflect and/or Revise (10 minutes):</b> Review of terms from today and prior labs: Algorithms, Procedures, Abstraction. See the Logo 1 exercise solutions below in the Assessments and Solutions section.  Students should write a reflection on their portfolio and complete the interactive exercises.
         <br/><b>Procedures and Parameters:</b>  In anticipation of the next Logo lesson, it might be useful in this lesson to discuss the power that procedures and parameters give us. Discuss how the practice of defining a procedures is a way of extending the language by incorporating a richer set of constructs (abstraction). Procedures enable us to encapsulate an algorithm into a single executable object that can be called or invoked whenever we need to perform the task that the algorithm does. Parameters enable us to make our procedures more general (and hence more abstract).   It should be easy with the Logo to see that the forward procedure is too specific because it moves the Android only 10 steps and that the forward(N) procedure is more general and hence more useful.</li>
    </ul>
    <h4>Other Resources:</h4>
    <ul>
    <li><a href="https://docs.google.com/a/css.edu/document/d/1rOwTpfDd_mm5O1UI6JlADYAWHTzUnmpgNg0kCBE7sUY/edit" target="_blank">Logo 1 Lesson Handout - Created by Joseph Kess, Wethersfield High School</a></li>
    <li> <a href="https://docs.google.com/document/d/122TCLup7PdG7wx43CJdk7vOQ-k1YsU3k1rc1uP9ePho/edit?usp=sharing" target="_blank">AP pseudocode compared to App Inventor Blocks</a> created by Timothy Clark,  Gilroy Unified School District (<a href="https://docs.google.com/document/d/1ObiA0u3Ipo9Cx30p3facy0j21oiw54L7vJkIpd7-Dys/edit?usp=sharing" target="_blank">landscape mode</a>).
    </li></ul>
    <div class="yui-wk-div" id="accordion">
    <h3 class="ap-classroom">AP Classroom</h3>
    <div class="yui-wk-div">
    <p>The College Board's <a href="http://myap.collegeboard.org" target="_blank" title="AP Classroom Site">AP Classroom</a> provides a question bank and Topic Questions. You may create a formative assessment quiz in AP Classroom, assign the quiz (a set of questions), and then review the results in class to identify and address any student misunderstandings.The following are suggested topic questions that you could assign once students have completed this lesson.</p>
    <p><b>Suggested Topic Questions:</b></p>
    <ul>
    <li>Topic 3.8 Iteration</li>
    <li>Topic 3.14 Libraries</li>
    </ul>
    </div>
    <h3 class="assessment">Assessment Opportunities and Solutions</h3>
    <div class="yui-wk-div">
    <p><b>Solutions</b> 
    <i>Note: Solutions are only available to verified educators who have joined the <a href="../Unit1-Getting-Started/PD-Joining-the-Forum.html" target="_blank">Teaching Mobile CSP Google group/forum in Unit 1</a>.</i></p>
    <ul>
    <li><a href="https://drive.google.com/open?id=1aeS-EHlTs5cZcX0Zs4MXFiaM6pfJf3GWeaKLqTU1XAs" target="_blank">Logo 1 Solutions</a>
    </li>
    <li><a href="https://drive.google.com/open?id=0B4W7CJ-1czH5aUZSQm9JRnJIOWc" target="_blank">Logo 1 aia file</a>
    </li>
    <li><a href="https://drive.google.com/open?id=1Us4_AJcI_9Xja_1lTTr6RJmI3Ko57W4Kisv7hmXv5cw" target="_blank">Quizly Solutions</a>
    </li>
    <li><a href="https://sites.google.com/umn.edu/mobilecspportfolioanswerkey/" target="_blank">Portfolio Reflection Questions Solutions</a>
    </li>
    </ul>
    <p><b>Assessment Opportunities</b></p>
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
    <div class="yui-wk-div">
    <p>If students are struggling with lesson concepts, have them review the following resources:</p>
    <ul>
    <li>Encourage them to test incrementally — adding only one feature to the face before they test their code</li>
    <li>Ensure they are using procedures for different parts of the face (each eye, the mouth, moving the turtle between steps, etc.). An example of the procedures they write could be:
            <ol>
    <li>drawFace</li>
    <li>moveToRightEye</li>
    <li>drawRightEye</li>
    <li>moveToLeftEye</li>
    <li>drawLeftEye</li>
    <li>moveToMouth</li>
    <li>drawMouth</li>
    </ol>
    </li>
    </ul>
    </div>
    <h3 class="diff-enrich">Differentiation: Enrichment</h3>
    <div class="yui-wk-div">
    <p>Students can add enhancements to their face, such as ears or eyeglasses. Students could also explore the use of <a href="http://appinventor.mit.edu/explore/ai2/support/blocks/control.html#forrange" target="_blank">for each loops</a> to improve their code.</p>
    </div>
    <h3 class="bk-knowledge">Background Knowledge: Algorithms &amp; Logo</h3>
    <div class="yui-wk-div">
    <ul>
    <li><b>Algorithms vs Recipes:</b> Algorithms vs. Recipes:  It's important to be a little careful with this distinction. Recipes are certainly like algorithms but many recipes would not count as algorithms (in computer science) because their statements are not precise enough.  So it is preferable to say that an algorithm is like a recipe rather an algorithm is a recipe.  We can revisit this distinction later on in the course when we talk about analyzing algorithms.  This is not to say that teachers should avoid using recipes to teach students about algorithms. There are lots of good lessons and exercises that use this approach. For example, one that seems to work well is to have students describe a recipe for making a PB&amp;J sandwich and then try to implement it (make PB&amp;Js to eat) and then discuss the ways in which their recipes failed to work -- mostly because steps were left out or steps were not precise enough.  This might be a good way of saying that for a recipe to be considered an algorithm, it would have to be so precise and each step so simple that it could be carried out by a machine.</li>
    <li><b>More on Logo and Turtles:</b> <a href="http://logothings.wikispaces.com/" target="_blank">Logo, Papert and Constructionist Learning</a></li>
    </ul>
    </div>
    <h3 class="tips">Teaching Tips: Incremental Testing</h3>
    <div class="yui-wk-div">
    <p>Emphasize that as programs become more complex, it is better to add features one at a time to a program then test, instead of adding all the features and testing at the end. Procedures can help manage the complexity of the program by encapsulating steps that work in a procedure and reducing the number of blocks in the main draw procedure.</p>
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
    <p>
    
.. poll:: mcsp-4-4-1
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


    
.. fillintheblank:: mcsp-4-4-2

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