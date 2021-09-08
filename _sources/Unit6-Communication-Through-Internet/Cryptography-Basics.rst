.. raw:: html 

   <div class="logo-header"  id="teacher-logo"  > <img class="align-center" src="../_static/Mobile_CSP_Logo_White_transparent.png" width="250px"/> </div>

Cryptography Basics
===================

.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
      $(document).ready(function() {
          generateFrameworkTable(EKmapping['6.06']);
          generateHovers();
      });
    
    </script>
    <p class="overview">
      After introducing students to cryptography in the preceding lesson using the Caesar Cipher app, <a href="https://runestone.academy/runestone/books/published/mobilecsp/Unit6-Communication-Through-Internet/Cryptography-Basics.html" target="_blank" title="">this lesson</a> 
      explores cryptography in depth through the study of additional ciphers. </p>
    <p>
      Information sent over the Internet is visible to others unless encrypted — but then it must also be decrypted so 
      the recipient can view it. Cryptography has ancient roots, increasing in complexity from the time of 
      Caesar to today's advanced systems. In this lesson students learn some basic principles of 
      cryptography by exploring some of the historically important cipher systems through several 
      hands-on activities.
    </p>
    <p> The overall goal of this and the follow-up lesson on cryptography is to reinforce the enduring 
      understanding that cybersecurity is an important concern for the Internet. An important principle to 
      be drawn from this lesson is that the story of cryptography is a never ending struggle between those
      who create ciphers to protect information and those who want to break the ciphers to gain access to
      secret information.  This battle is playing out today -- think of the debate between the FBI and Apple
      over iPhone encryption.  This lesson presents that back-and-forth story through historical examples of 
      actual ciphers.
    </p>
    <p>
      Several encryption algorithms
      are presented as well as several strategies (attacks) for breaking ciphers.  The several activities
      provide students a hands-on way to experience these.  However, students are not expected to memorize 
      the algorithms or to be able to apply them on
      an exam.  The College Board guideline states that the specific mathematical functions used in cryptography
      are beyond the scope of this course.
    </p>
    <table border="" class="framework" id="genTable" width="100%"></table>
    <div class="pd yui-wk-div">
    <h3>Professional Development</h3>
    <p><b>The Student Lesson:</b> Complete the activities for <a href="https://runestone.academy/runestone/books/published/mobilecsp/Unit6-Communication-Through-Internet/Cryptography-Basics.html" target="_blank" title="">Mobile CSP Unit 6: Lesson 6.6 Cryptography Basics</a>.
      </p>
    </div>
    <h3>Materials</h3>
    <ul>
    <li><a href="https://docs.google.com/presentation/d/1GOzrwChWLjWbYi_yqKpLi2T60dwM8Yv2CaX2qGPzuV8/edit#slide=id.p5" target="_blank" title="">Slides</a>: This is a long slide deck (77 slides) but should be broken into several parts and
         interspersed with activities, as described below.
      </li>
    <li>There are four short video clips in this lesson:  Video 1, Substitution Cipher (1:52),
        Video 2, Frequency Analysis (3:28), Video 3, Vigenere cipher (3:38), and Video 4, Key exchange problem (6:07).  
      </li>
    <li><a href="http://csunplugged.org/wp-content/uploads/2014/12/unplugged-16-information_hiding_0.pdf" target="_blank">CS Unplugged Information Hiding Activity</a> - requires pad of paper and pen/pencil</li>
    <li>Computer lab with projection system</li>
    <li>Optional: <a href="https://drive.google.com/open?id=1NjfrC9q6b4hvSOP-35P7Pfg_us9jo4TB" target="_blank">Caesar Cipher Wheel</a> printouts and scissors and paper fasteners to make them.
    </li></ul>
    

Learning Activities
--------------------

.. raw:: html

    <p>
    <h3 id="est-length">Estimated Length: 90 minutes</h3>
    <ul>
    <li><b>Hook/Motivation (10 minutes):</b> Complete the CS Unplugged <a href="http://csunplugged.org/wp-content/uploads/2014/12/unplugged-16-information_hiding_0.pdf" target="_blank">Information Hiding</a> exercise.</li>
    <li><b>Experiences and Explorations (70 minutes):</b>
    <ul>
    <li><b>Part 1 - Simple Substitution Cipher:</b> Using the slides (14-17) or Video 1 (1:52) discuss the fact
            that Caesar cipher is a fairly trivial example of a substitution cipher -- i.e., very easy to crack.  
            Describe in general how a simple substitution cipher works. Have the students practice with the 
            interactive exercise.
          </li>
    <li><b>Part 2 - Frequency Analysis:</b> Using the slides (18-31) or Video 2 (3:28)  discuss how frequency 
            analysis can be used to break encrypted text and how transposition ciphers work. Have the students 
            practice with the interactive exercise and the question listed after. (Hint: they can paste 
            the text into the interactive question to see a histogram. Examine the occurrences of common 
            letters such as vowels and s, t, etc. to help you figure out which is which.)
          </li>
    <li><b>Part 3 - Vigenere Cipher:</b> Using the slides (32-55) or Video 3 (3:38) discuss how a 
            Vigenere cipher works. Have the students practice with the interactive exercise.
          </li>
    <li><b>Part 4 - Perfect Secrecy and the Key Exchange Problem (10 minutes):</b> Using the 
            slides (56-77) or Video 4 (6:07) describe how the Vigenere Cipher can be broken and some strategies to 
            prevent it. This topic will be continued in a later lesson that looks at a more 
            sophisticated technique for encryption.
          </li>
    </ul>
    </li>
    <li><b>Rethink, Reflect and/or Revise (10 minutes):</b> Have students complete the interactive 
        exercises and portfolio reflections</li>
    </ul>
    <div class="yui-wk-div" id="accordion">
    <h3 class="ap-classroom">AP Classroom</h3>
    <div class="yui-wk-div">
    <p>The College Board's <a href="http://myap.collegeboard.org" target="_blank" title="AP Classroom Site">AP Classroom</a> provides a question bank and Topic Questions. You may create a formative assessment quiz in AP Classroom, assign the quiz (a set of questions), and then review the results in class to identify and address any student misunderstandings.The following are suggested topic questions that you could assign once students have completed this lesson.</p>
    <p><b>Suggested Topic Questions:</b></p>
    </div>
    <h3 class="assessment">Assessment Opportunities</h3>
    <div class="yui-wk-div">
    <p><b>Solutions:</b></p>
    <ul>
    <li>Note: Solutions are only available to verified educators who have joined the <a href="./unit?unit=1&amp;lesson=39" target="_blank">Teaching Mobile CSP Google group/forum in Unit 1</a>.</li>
    <li><a href="https://drive.google.com/open?id=1Us4_AJcI_9Xja_1lTTr6RJmI3Ko57W4Kisv7hmXv5cw" target="_blank">Quizly Solutions</a>
    </li>
    <li><a href="https://sites.google.com/a/css.edu/jrosato-cis-1001/" target="_blank">Portfolio Reflection Questions Solutions</a>
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
    <li><a href="https://www.khanacademy.org/math/applied-math/cryptography/crypt/v/intro-to-cryptography?v=Kf9KjCKmDcU" target="_blank">Khan Academy video on encryption, decryption, and ciphers</a></li>
    <li><a href="http://www.youtube.com/watch?v=SAAflrIp__E" target="_blank">TED Talk by James Lynn</a> that connects cryptography and Internet security</li>
    <li>Khan academy's <a href="https://www.khanacademy.org/math/applied-math/cryptography/crypt/v/caesar-cipher?v=sMOZf4GN3oc" target="_blank">Caesar cipher and frequency analysis video</a></li>
    </ul>
    </div>
    <h3 class="diff-enrich">Differentiation: Enrichment</h3>
    <div class="yui-wk-div">
    <ul>
    <li>You can find more cryptography challenges at <a href="https://cryptoclub.org" target="_blank">CryptoClub.org</a>.</li>
    <li>Here is a crypto challenge game at <a href="https://www.khanacademy.org/computing/computer-science/cryptography/cryptochallenge/a/cryptochallenge-introduction" target="_blank">Khan Academy</a>.</li>
    <li><i>The Code Book</i> by Simon Singh is an in-depth history of encryption and its relationship to computer science.</li>
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
    <li>While encryption techniques used with the Internet will be introduced in a later lesson, this lesson points out common concerns with any encryption technique. What are they and how can you make the connection to information on the Internet?</li> <!-- for an EU -->
    </ul>
    <!-- These are the PD exit slips.  We should have corresponding exit slips for use after the classroom lesson. -->
    
.. poll:: mcsp-6-6-1
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


    
.. fillintheblank:: mcsp-6-6-2

    What questions do you still have about the lesson or the content presented? |blank|

    - :/.*/i: Thank you. We will review these to improve the course.
      :x: Thank you. We will review these to improve the course.


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    </div>
    </div>