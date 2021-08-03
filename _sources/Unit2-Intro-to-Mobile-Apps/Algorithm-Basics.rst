.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Algorithm Basics
================

.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
      $(document).ready(function() {
          generateFrameworkTable(EKmapping['2.03']);
          generateHovers();
      }); 
    </script>
    <!-- This is the overview paragraph.  The link URL should be to the corresponding lesson on the student branch. -->
    <p class="overview">
    <a href="https://runestone.academy/runestone/books/published/mobilecsp/Unit2-Intro-to-Mobile-Apps/Algorithm-Basics.html" target="_blank" title="">This lesson</a> focuses on the concepts of algorithms and programming, which is one of the course's big ideas. As one of the many lessons in the course on algorithms, it begins by providing a definition and introducing some of the fundamental building blocks that are used to construct algorithms. They will use the three fundamental constructs for building algorithms: sequence, a sequence of statements; selection, a branching between two alternative statements; and repetition, a loop that repeats statements. Students will evaluate and write algorithms using pseudocode, which is part of the AP Exam, and make connections to App Inventor. This lesson reinforces the enduring understanding that algorithms are precise sequences of instructions for processes that can be executed by a computer and are implemented using programming languages. Also, in this lesson students will complete a group work activity using the POGIL structure. (POGIL stands for Process-Oriented Guided Inquiry Learning; more information is provided in the background knowledge and teaching tips sections below and in the <a href="https://runestone.academy/runestone/books/published/teach-mobilecsp/Unit10-Inclusive-Teaching/toctree.html" target="_blank">pedagogy lesson</a> in Unit 10.) </p>
    <!-- This is the framework table, where we describe how this lesson fits into the CSP framework.  -->
    <table border="" class="framework" id="genTable" width="100%"></table>
    <div class="pd yui-wk-div">
    <h3>Professional Development</h3>
    <p><b>The Student Lesson:</b> Complete the activities for 
        <a href="https://runestone.academy/runestone/books/published/mobilecsp/Unit2-Intro-to-Mobile-Apps/Algorithm-Basics.html" target="_blank" title="">Mobile CSP Unit 2 Lesson 2.3: Algorithm Basics</a>.
      </p>
    </div>
    <h3>Materials</h3>
    <p></p><ul><li>Projection System</li><li><a href="https://docs.google.com/presentation/d/1XfwXHnhzIxQQppKgxS6PAhc9f61LHeLcILd6feAHc8E/edit" target="_blank">Slides</a></li><li><a href="https://drive.google.com/open?id=1_NfNLWJxaG4qZ2Jd2x8UctDS05twn1h6p-o3XaAcRv0" target="_blank">POGIL role cards</a></li><li><a>Worksheet for POGIL Activity</a></li></ul><p></p>
    

Learning Activities
--------------------

.. raw:: html

    <p>
    <h3 id="est-length">Estimated Length: 45 minutes</h3>
    <ul style="clear:both">
    <li><b>Hook/Motivation (5 minutes):</b> Ask the students to define what an algorithm is. <b>Explanation:</b> Provide the definition of an algorithm: An algorithm is a sequence of precise instructions, a step-by-step procedure, that solves some problem or does some computation. Next, review the Blockly Maze activity as needed, emphasizing that there are multiple solutions to the problems, but that some may be more efficient than others as well as reinforcing the concepts of sequence, selection and repetition types of control structures.</li>
    <li><b>Experiences and Explorations (30 minutes):</b>
    <ul>
    <li>Lecture (10 minutes): Use the slide presentation to provide an overview of algorithms to the students</li>
    <li>POGIL Roles and Teams (5 minutes): Divide students into groups of 3-4 teams. Review the POGIL structure and roles with the students, having groups assign each member a role. Since this is the first time using the POGIL format, you might find it useful to distribute the <a href="https://docs.google.com/document/d/1_NfNLWJxaG4qZ2Jd2x8UctDS05twn1h6p-o3XaAcRv0/edit?usp=sharing" target="_blank">POGIL role cards</a> to the groups. Be sure to emphasize that POGIL has been shown to help students learn the concepts better and that most students prefer this format. </li><li>POGIL Activity (15 minutes) In the POGIL teams, students should work through the critical thinking questions. Make sure that they identify the complete repetition and selection structures, not just the first line of each. The answers to the POGIL questions are in the Assessment section below. Look ahead at the answers to anticipate questions you may be asked.
          
           
           </li>
    </ul>
    </li>
    <li><b>Rethink, Reflect and/or Revise (10 minutes):</b> Have the students complete the interactive questions and their portfolio reflection.</li>
    </ul>
    <div class="yui-wk-div" id="accordion">
    <h3 class="ap-classroom">AP Classroom</h3>
    <div class="yui-wk-div">
    <p>The College Board's <a href="http://myap.collegeboard.org" target="_blank" title="AP Classroom Site">AP Classroom</a> provides a question bank and Topic Questions. You may create a formative assessment quiz in AP Classroom, assign the quiz (a set of questions), and then review the results in class to identify and address any student misunderstandings.The following are suggested topic questions that you could assign once students have completed this lesson.</p>
    <p><b>Suggested Topic Questions:</b></p><ul><li><span style="font-weight: 400;">Topic 3.6 Conditionals</span></li></ul></h4>
    </div>
    <h3 class="assessment">Assessment Opportunities and Solutions</h3>
    <div class="yui-wk-div">
    <p><b>Solutions:</b></p>
    <ul>
    <li>Note: Solutions are only available to verified educators who have joined the <a href="./unit?unit=1&amp;lesson=39" target="_blank">Teaching Mobile CSP Google group/forum in Unit 1</a>.</li>
    <li><a href="https://drive.google.com/open?id=1Us4_AJcI_9Xja_1lTTr6RJmI3Ko57W4Kisv7hmXv5cw" target="_blank">Quizly Solutions</a>
    </li>
    <li><a href="https://sites.google.com/a/css.edu/jrosato-cis-1001/" target="_blank">Portfolio Reflection Questions Solutions</a>
    </li>
    </ul>
    <p>The POGIL exercise solutions are below:
       
             </p><ol>
    <li>CAN_MOVE(forward) is true. CAN_MOVE(right) is false.</li>
    <li><pre>  
      MOVE_FORWARD
      MOVE_FORWARD
      ROTATE_RIGHT
      MOVE_FORWARD
      MOVE_FORWARD
      MOVE_FORWARD
      MOVE_FORWARD
      ROTATE_LEFT
      MOVE_FORWARD
      MOVE_FORWARD</pre>
    </li>
    <li><pre>           
    REPEAT 2 TIMES 
      {
        MOVE_FORWARD
      }
      ROTATE_RIGHT
      REPEAT 4 TIMES 
      {
        MOVE_FORWARD
      }
      ROTATE_LEFT
      REPEAT 2 TIMES
      {
        MOVE_FORWARD
      }
      
               </pre>
    </li><li><ul><li>Example of Selection:IF CAN_MOVE forward
                 MOVE_FORWARD;</li> <li>Example of Repetition: <pre>REPEAT UNTIL GoalReached
      IF CAN_MOVE forward
        MOVE_FORWARD
      IF CAN_MOVE left
         ROTATE_LEFT  
      IF CAN_MOVE right
         ROTATE_RIGHT</pre>
    </li>
    <li>Most students will say the algorithm works for this maze in 10 iterations since there are 10 commands needed. However, you should point out in class discussion that the loop body actually runs for 8 iterations, because sometimes you can do 2 commands inside the loop if you can move forward and then rotate_right or left. After the first if statement is finished, we sequentially move down to the next if statement, and it can be executed right away if it is true. So, the 2 turns are done right after a move_forward in the same iteration of the loop. You could even say that the loop condition at the top runs for the 9th and final time to exit the loop. </li>
    <li>The algorithm will get stuck in mazes where there is a dead end and the robot needs to turn back to find another way. The robot will not be able to turn back, because to rotate, the space to its right or left needs to be available. </li>
    </ul>
    </li>
    <li><pre>           REPEAT 10 times
                 IF cup
                    hot_wash
                 IF dish
                    cold_wash
                  </pre></li>
    </ol>
    </div>
    <h3 class="diff-practice">Differentiation: More Practice</h3>
    <div class="yui-wk-div">
    <p>Have students be the robot themselves, putting squares of paper on the floor to represent the maze. One student can read off the algorithm while another student "executes" the commands by walking through the maze. Alternatively, a student could walk the maze and then write the algorithm from it.</p>
    <p>Here are some additional resources if students are struggling with lesson concepts:</p>
    <ul>
    <li>Algorithms: Have them complete more of the Blockly Maze activities, asking them to identify which mazes they use sequence, selection, and repetition concepts.</li>
    <li>Pseudocode: Show students the <a href="https://drive.google.com/file/d/0B5ZVxaK8f0u9c1VlWFJDRHl0dEk/view?usp=sharing" target="_blank" title="">AP Exam Reference Sheet</a> as it has some common pseudocode commands that they can use to help write their own pseudocode. (Students can access it directly in <a href="https://mobilecsp-2017.appspot.com/mobilecsp/unit?unit=127&amp;lesson=130" target="_blank">Lesson 8.2</a>.).</li><li><span class="yui-non">Pseudocode: pHave students try ractice questions on <a href="https://www.khanacademy.org/computing/ap-computer-science-principles/ap-csp-exam-preparation/prepare-for-the-2019-ap-cs-p-exam/a/ap-csp-exam-pseudocode-reference" target="" title="">Khan Academy</a>.</span></li><li><span class="yui-non">Guess your birthday (day and month) using math calculations. Have students watch this <a href="https://www.youtube.com/watch?v=MaFgHSAGbwU" target="_blank" title="">birthday calculation video</a> and have them practice writing the algorithm. Students can swap algorithms with a classmate to see if their algorithm is correct and works to calculate their birthday.</span></li>
    </ul>
    </div>
    <h3 class="diff-enrich">Differentiation: Enrichment</h3>
    <div class="yui-wk-div">
    <p>One idea is to have the students write an algorithm for opening a locker with a combination lock. Another idea is to have the students write an algorithm, in pseudocode, for how they eat lunch. See <a href="https://docs.google.com/a/css.edu/viewer?a=v&amp;pid=sites&amp;srcid=ZGVmYXVsdGRvbWFpbnxld2Rtb2JpbGV8Z3g6M2I1NmE1NDY1ZGM1ZmMyNA" target="_blank">Betsy Dillard's example assignment</a>. Ask students to compare different algorithms. Is an algorithm that takes fewer steps better? more efficient? Is there a difference in difference in clarity between two algorithms? This should be a brief introduction. Students do not need to understand this yet. But, they should start thinking about it. Efficiency and clarity will be taught in the Analyzing Algorithms lesson. If using the base conversion example, you could discuss the questions above in terms of base conversion algorithms. You could also have students compare the algorithms they wrote in class.</p>
    </div>
    <h3 class="bk-knowledge">Background Knowledge: More on Algorithms</h3>
    <div class="yui-wk-div">
    <ul>
    <li>Iteration and repetition both refer to loop structures in programming.</li>
    <li>Wikipedia has a nice explanation on <a href="http://en.wikipedia.org/wiki/Algorithm" target="_blank">Algorithms</a> and <a href="http://en.wikipedia.org/wiki/Pseudocode" target="_blank">Pseudocode</a>.</li>
    <li>Computer Science Fact: <a href="http://en.wikipedia.org/wiki/Structured_program_theorem" target="_blank">It has been proven</a> that sequence, selection, and repetition are the only control structures needed to build any algorithm that can be thought of. In other words, any algorithm can be expressed using only sequence, selection, and repetition. So, the students have already been introduced to all of the algorithm building tools they would need to solve any computing problem that can be solved. (This is not to say every computing problem can be solved -- that's another story.)</li>
    </ul>
    </div>
    <h3 class="bk-knowledge">Background Knowledge:  POGIL</h3>
    <div class="yui-wk-div">
    <p>POGIL, Process Oriented Guided Inquiry Learning, as used in Mobile CSP, is a structured cooperative learning approach where students work in teams of 3-4 students to solve problems. <a href="https://pogil.org/about/effectiveness" target="_blank">Research suggests</a> that the POGIL approach helps students master the content more effectively and that most students prefer to learn in POGIL teams over more traditional approaches. <a href="https://vimeo.com/93407527" target="_blank">This video</a> provides an overview of POGIL. Learn more about the <a href="https://pogil.org/about" target="_blank">POGIL Project</a> and POGIL being used in <a href="http://cspogil.org/tiki-index.php" target="_blank">computer science courses</a>.</p>
    </div>
    <h3 class="tips">Teaching Tip:  Algorithm Vocabulary</h3>
    <div class="yui-wk-div"><p>In this lesson and future lessons, make sure that you revisit the terms sequence, selection, and repetition, especially when programming in App Inventor.</p></div>
    <h3 class="tips">Teaching Tip:  Pseudocode for More Practice</h3>
    <div class="yui-wk-div"><p>If students are struggling with writing App Inventor code, encourage them to express their ideas by: 1) explaining it out loud to someone else and 2) writing the pseudocode for the algorithm.</p></div>
    <h3 class="tips">Teaching Tip:  Enforcing POGIL Roles</h3>
    <div class="yui-wk-div">
    <p>One key to POGIL being effective in the classroom is ensuring that students are participating cooperatively - each student is assuming responsibility for their role in the group. As students are working, teachers should be moving around the room and listening to groups to make sure that students are not only staying on task with activities, but are also actively fulfilling their roles. You can print and distribute the <a href="https://docs.google.com/document/d/1_NfNLWJxaG4qZ2Jd2x8UctDS05twn1h6p-o3XaAcRv0/edit?usp=sharing" target="_blank">role cards</a> to each group, or even post them in your classroom for easy reference.</p>
    </div>
    </div> <!-- accordion -->
    <div class="pd yui-wk-div">
    

Professional Development Reflection
------------------------------------

.. raw:: html

    <p>
    <p>Discuss the following questions with other teachers in your professional development program.</p>
    <ul>
    <li>How do the lesson activities reinforce the idea that algorithms are precise sequences of instructions that can be executed on a computer? </li>
    <li>In this course we will building and analyzing algorithms throughout our study of computer science. Is there anything else you would need to have or know to teach this lesson effectively? What specific elements of this lesson (examples, activities, etc.) would you change? How would you modify or add to the interactive exercises (formative assessments)?
        </li>
    <li>How does the use of POGIL reinforce the computational thinking practices of communication and collaboration? </li>
    </ul>
    <!-- These are the PD exit slips.  We should have corresponding exit slips for use after the classroom lesson. -->
    <p>
    
.. poll:: mcsp-2-3-1
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


    
.. fillintheblank:: mcsp-2-3-2

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