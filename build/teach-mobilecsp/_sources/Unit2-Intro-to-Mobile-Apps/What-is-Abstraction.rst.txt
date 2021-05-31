.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

What is Abstraction
===================

.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
      $(document).ready(function() {
          generateFrameworkTable(EKmapping['2.08']);
          generateHovers();
      }); 
    
    </script>
    <!-- This is the overview paragraph.  The link URL should be to the corresponding lesson on the student branch. -->
    <p class="overview">
    <a href="https://course.mobilecsp.org/mobilecsp/unit?unit=1&amp;lesson=61" target="_blank" title="">This lesson </a> 
      introduces the concept of abstraction, which is one of the seven big ideas.  This will be one of many lessons in the course that focuses on abstraction.  In this first look, the focus is on the everyday concept and promotes the idea hat the process of abstraction is a fundamental element of human thought and language.  Through a number of examples of abstraction in everyday life as well as in computing, students explore and reflect on what abstraction is and how it is exemplified in their own worlds.  This lesson also makes an initial connection to how abstraction is used in programming. The examples of an App Inventor variable and an App Inventor procedure are shown as examples of <i>data abstraction</i> and <i>procedural abstraction</i> respectively, thereby reinforcing the enduring understanding that abstractions are a fundamental element of building computer programs and other computational artifacts. 
    </p>
    <!-- This is the framework table, where we describe how this lesson fits into the CSP framework.  -->
    <table border="" class="framework" id="genTable" width="100%"></table>
    <div class="pd yui-wk-div">
    <h3>Professional Development</h3>
    <p><b>The Student Lesson: </b> Complete the activities for 
        <a href="https://course.mobilecsp.org/mobilecsp/unit?unit=1&amp;lesson=61" target="_blank" title="">Mobile CSP Unit 2 Lesson 2.8: What is abstraction?</a>.
      </p>
    </div>
    <h3>Materials</h3>
    <ul>
    <li>Projection system</li><li>Piece of blank paper for each student</li><li>Writing instrument for each student</li><li><a href="https://docs.google.com/a/css.edu/presentation/d/1nOMpxZpdkCcS6Wc-eU8eeBi-z55LyKSJRBCVolJDM78/edit" target="_blank">Slides</a><br/></li>
    </ul>
    

Learning Activities
--------------------

.. raw:: html

    <p>
    <h3 id="est-length">Estimated Length: 45 minutes</h3>
    <h4>Hook/Motivation (10 minutes)</h4>
    <ul>
    <li><b>Activity:</b> Ask each student to take a piece of paper and without talking communicate to the class what 'chair' means. Students may use words, phrases, pictures, etc but they cannot talk. When the students are finished have the students hold up their papers to show the entire class. Next, ask the students to do the same thing for 'rectangle'. What do the students notice about what they have put on their papers?
      Other ideas for a hook are playing 20 questions where you go from a more abstract description of something to more and more specific, or asking students what they ate for breakfast where breakfast is an abstract term that can stand for many different specific food items. </li>
    <li><b>Explanation:</b> Explain: All of the students' answers are correct. This is because 'chair' and 'rectangle' are both abstractions</li>
    <ul>
    <li>Abstraction can be looked at in two ways, as a practice or a habit of mind, sometimes called abstracting or as a particular thing, such as an idea or a word where we say, for example, that the word 'chair' is an abstraction. The words 'chair' and 'rectangle' represent an idea of something.</li>
    <li>We refer to anything that we can sit in as a 'chair'. But, there are different kinds of chairs (e.g. desk chairs, office chairs, wooden chairs, rolling chairs, etc.) When we say 'chair' we can mean any one of these.</li>
    <li>Any shape that has 4 sides and 4 right angles, with opposite sides of equal length, is a 'rectangle'. But, there are different kinds of rectangles (e.g. 4x6 rectangles, 2x6 rectangles, 3x9 rectangles, etc) When we say 'rectangle' we can mean any one of these.</li>
    </ul>
    </ul>
    <h4>Experiences and Explorations (25 minutes)</h4>
    <ul>
    <li><b>Lecture: </b> Topic: Abstraction (<a href="https://docs.google.com/a/css.edu/presentation/d/1nOMpxZpdkCcS6Wc-eU8eeBi-z55LyKSJRBCVolJDM78/edit" target="_blank">Slides</a>)
    <p>Use this presentation to give a brief explanation of abstraction with some examples. Explain to students that an abstraction is a general representation or concept or idea that stands for some collection of individual instances. Abstractions can be found in language, design, maps, and computer science.
    </p><p>Explanation: The students will learn variables, procedures, and data abstraction while in the course. In the next lesson, the students will begin learning data abstraction which includes bits and binary numbers. 
      
      </p></li>
    <!--
      &lt;p&gt;First, let’s think about abstraction as a practice. As mental agents we are constantly bombarded through our senses by sensations -- i.e., sights and sounds and tactile sensations. Somehow our brains condense these raw data into simple recognizable constructs that we can use to function in the world. For example, when I look out the window, I recognize various objects – trees, birds, and flowers – that my brain has constructed for me out of the raw signals (light waves) that come in through my eyes. It requires no mental effort on my part to see a tree. Similarly, our ability to give names to things – the word ‘tree’ – and then use the names in our language and thought is good example of abstracting as a habit of mind.
    &lt;/p&gt;&lt;p&gt;Thus, as a practice or habit of mind, abstracting is the process of simplifying or condensing large amounts of data into manageable chunks. We have various names for these chunks depending on how they are used – e.g., ideas, concepts, words, and so on. But in this sense abstracting is a fundamental element of human cognition and language. We could neither think nor speak if our brains couldn&#39;t create abstractions.
    &lt;/p&gt;&lt;p&gt;Let’s now think about the result of this abstracting process – the ideas and concepts and words that we manipulate in our everyday thought and language. An abstraction in this sense is a general representation that stands for some complex collection of individual instances. One of the main characteristics of an abstraction is that it simplifies a complex phenomenon by leaving out the irrelevant aspects. When our brain creates the perception of a tree, it ‘abstracts away’ many of the details, its color, its species, its height and so on. Of course what is ‘irrelevant’ only has meaning in a certain context. For a botanist, a tree’s species is very important so perhaps when a botanist sees a tree, he or she always sees an oak tree or a maple tree. Most of us just see a tree. One of the main characteristics of an abstraction is that when viewed from the perspective of an individual instance, it leaves out certain non-essential details. In creating an abstraction we &#39;abstract away&#39; certain details of the instances we&#39;re trying to represent. This &#39;abstracting away&#39; is a fundamental habit of mind, a low-level feature of human cognition and language. We could neither speak nor think if we weren&#39;t able to create and manipulate abstractions.
    &lt;/p&gt;&lt;p&gt;In order to understand and use an abstraction, we need to understand the context in which it is used. 
    &lt;/p&gt;&lt;/li&gt;-->
    <li><b>Activity:</b> After the lecture/class discussion, have students work in pairs to draw abstract objects for each other to guess and to look at the <a href="https://www.google.com/search?q=calculator" target="_blank">Google scientific calculator</a> to identify the functions associated with abstract buttons such as + and -. 
    </li></ul>
    <h4>Rethink, Reflect and/or Revise (10 minutes):</h4>
    <ul>
    <li>Ask the students to complete the interactive exercises on the Mobile CSP lesson.</li>
    <li>Briefly review the major ideas of the lesson with students. Provide an “exit slip” that asks students to write down one major idea they learned today along with one question they still have. Collect the slips and use them to review any misconceptions or answer any questions before the next lesson.</li>
    <li>Exit slip example:
        <ul>
    <li>Provide one interesting/compelling idea that you learned today.</li>
    <li>What is one idea or concept that is unclear? </li>
    </ul>
    </li>
    </ul>
    <div class="yui-wk-div" id="accordion">
    <h3 class="ap-classroom">AP Classroom</h3>
    <div class="yui-wk-div">
    <p>The College Board's <a href="http://myap.collegeboard.org" target="_blank" title="AP Classroom Site">AP Classroom</a> provides a question bank and Topic Questions. You may create a formative assessment quiz in AP Classroom, assign the quiz (a set of questions), and then review the results in class to identify and address any student misunderstandings.The following are suggested topic questions that you could assign once students have completed this lesson.</p>
    <h4>Suggested Topic Questions: <span style="font-weight: normal;">None</span></h4>
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
    <h3 class="diff-practice">Differentiation: More Practice</h3>
    <div class="yui-wk-div">
    <p>(Suggested by Joan Goldberg) Have students play a game such as Guess Who or 20 Questions. Afterwards, 
    explain how the person or thing they were trying to guess was very abstract in the beginning but became
    more concrete as they discovered more details through the questioning.</p>
    </div>
    <h3 class="bk-knowledge">Background Knowledge: Everyday Examples of Abstraction</h3>
    <div class="yui-wk-div">
    <p>Here are some everyday examples of abstraction.</p>
    <ul>
    <p><u>Language example:</u>  A definition of any word we use in our language -- e.g., 'chair' -- is an abstraction.  When we define 'chair' -- or cognitively think of a chair -- we don't think of its color or what type of material its made of. The word or idea is a <b><i>general representation</i></b> of chairs.  A name is sort of the ultimate abstraction. It's just a simple symbol that represents an individual.  Imagine what life and language would be like if we had to give a detailed description every time we wanted to refer to someone?
        </p>
    <p><u>Design example:</u>  If you were remodeling your kitchen you might create a schematic model of the floor plan with rectangles or squares to represent the size and location of the appliances.  The model is a<b><i> general representation</i></b> of an actual kitchen and its appliances.  Among other things, we've 'abstracted away' the brand and color of the appliances and the entire Z-axis, if we're doing this in a 2-d model (bird's eye view).
        </p>
    <p><u>Map example:</u>  Think of a hand-drawn map.  It's a <b><i>general representation</i></b> of some particular geographical region in which we've abstracted away the actual dimensions, foliage, etc. The abstraction contains just those details that we need to get us from point A to point B.
        </p>
    <p>What does this have to do with the study of computer science?<b>   In computer science the process of abstracting – simplifying, condensing, encapsulating – is an important problem solving technique that is used in designing computer systems from the lowest levels of the hardware to the highest levels of the software.</b>  And, as we will see in this course, computer scientists constantly strive to create abstractions, in hardware and software, <span style="font-weight: bold;">that help reduce complexity and make computer systems and computer programs easier to use and understand.</span>
    </p>
    <p>In this course we will deal with two main types of abstraction, <span style="font-style: italic;">data abstraction</span> and <span style="font-style: italic;">procedural abstraction</span>. Here are a couple of brief examples
        </p>
    <p><span style="text-decoration: underline;">Data Abstraction</span>.  In a computer program a <span style="font-style: italic;">variable </span>is named section of memory, e.g., ‘X’, that can store a piece of data – i.e., a number or a word or a list of objects. When we want to manipulate the data, we can use its name rather than the data itself.  So the name, the variable, is an abstraction of the data stored in the variable.  Using the name, rather than the data itself, simplifies things for the programmer, especially because the data stored in the variable can change.
        </p>
    <p>There’s another sense in which the variable is an abstraction. First, inside the computer’s memory, everything is stored as electronic signals, on or off, high voltage or low voltage.  It’s hard to see electronic signals or write them on a piece of paper.  So computer scientists represent those electronic signals as <span style="font-weight: bold; font-style: italic;">bits</span>, <span style="font-weight: bold; font-style: italic;">bi</span>nary dig<span style="font-weight: bold; font-style: italic;">its</span> – i.e., 0s and 1s. So bits are a higher-level of abstraction and, as such, easier for us to deal with.  But strings of bits – 000100010100010 – are relatively hard for most people to manipulate.  We prefer to deal with higher-level symbols, such as decimal numbers (5) and words (tree) and lists of numbers ([1,2,3,4,5]). These then, are <span style="font-style: italic;">higher-level abstractions</span> that make it easier for us to manipulate data. [There are different levels of abstraction, for example, using words vs. using pictures vs. using bits (where words are at the highest level - the easiest for us to understand- and bits are at a lower level.) The next abstraction lesson Adding 1+1=2 covers this in more detail by explaining to students how a computer adds 1+1.)] Finally, because these data can change within the computer’s memory, we use variables to achieve an even higher level of abstraction.  In effect, the variable lets us say ‘take whatever data are stored in X and put it in Y.’
        </p>
    <p><span style="text-decoration: underline;">Procedural Abstraction</span>.  A <span style="font-style: italic;">procedure </span>is a named chunk of code that performs a particular task.  An example might be the square root procedure, which calculates the square root of <span style="font-style: italic;">X, sqrt(X)</span>.  The nice thing about procedures is that they hide the details of how they carry out their task.  For example, we may no longer remember how to calculate a square root by hand, but we do know how to use the <span style="font-style: italic;">sqrt() </span>procedure (on a computer or a calculator) to calculate the square root of any number:  I simply call it and give it the number.  So <span style="font-style: italic;">sqrt(4)</span>  is 2. And <span style="font-style: italic;">sqrt(5)</span> is 2.236. 
        </p>
    <p>The <span style="font-style: italic;">sqrt()</span> procedure is an abstraction. It encapsulates a complex task and gives us the ability to perform that task without worrying about the details of how it works. It ‘abstracts away’ the details of how to calculate a square root.   And just like with data abstraction, procedures can be organized into levels of abstraction.  For example, if you remember your Pythagorean theorem you will recall that the “length of the hypotenuse of a right triangle is the square root of the sum of the squares of the other two sides.”  So, once we have low-level procedures, such as <span style="font-style: italic;">sqrt(X)</span>, we can use them to define <span style="font-style: italic;">higher-level procedures</span> such as <span style="font-style: italic;">hypotenuse(a,b)</span>.  Then to calculate the hypotenuse of a 3-4-5 right triangle, we can just call <span style="font-style: italic;">hypotenuse(3,4)</span>  and it will give us the value 5.
        </p>
    </ul>
    </div>
    </div> <!-- accordion -->
    <div class="pd yui-wk-div">
    

Teacher PD Reflection
----------------------

.. raw:: html

    <p>
    <p>Discuss the following questions with other teachers in your professional development program.</p>
    <ul>
    <li>How do the lesson activities reinforce the concept of abstraction?</li>
    <li>In this course we will see many examples of abstraction throughout our study of computer science.
    Is there anything else you would need to have or know to teach this lesson effectively?
    What specific elements of this lesson (examples, activities, etc.) would you change?
          How would you modify or add to the interactive exercises (formative assessments)?</li>
    </ul>
    <!-- These are the PD exit slips.  We should have corresponding exit slips for use after the classroom lesson. -->
    <p>
    
.. mchoice:: mcsp-2-8-1
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


    
.. fillintheblank:: mcsp-2-8-2

    What questions do you still have about the lesson or content presented? |blank|

    - :/.*/i: Thank you. We will review these to improve the course content.
      :x: Thank you. We will review these to improve the course content.


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    </p>
    </div>
    </div>