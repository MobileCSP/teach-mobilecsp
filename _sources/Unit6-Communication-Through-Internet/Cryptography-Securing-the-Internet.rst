.. raw:: html 

   <div class="logo-header"  id="teacher-logo"  > <img class="align-center" src="../_static/Mobile_CSP_Logo_White_transparent.png" width="250px"/> </div>

Cryptography Securing the Internet
==================================

.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
     $(document).ready(function() {
          generateFrameworkTable(EKmapping['6.07']);
          generateHovers();
      }); 
    
    </script>
    <p class="overview"><a href="https://runestone.academy/runestone/books/published/mobilecsp/Unit6-Communication-Through-Internet/Cryptography-Securing-the-Internet.html" target="_blank">This lesson</a> continues the topic of cryptography, examining cryptographic techniques used to secure data on the Internet. A key concept introduced is that of public and private keys and combining them to ensure secure communication.</p>
    <table border="" class="framework" id="genTable" width="100%"></table>
    <div class="pd yui-wk-div">
    <h3>Professional Development</h3>
    <p><b>The Student Lesson:</b> Complete the activities for <a href="https://runestone.academy/runestone/books/published/mobilecsp/Unit6-Communication-Through-Internet/Cryptography-Securing-the-Internet.html" target="_blank">Unit 6: Lesson 6.7 Cryptography: Securing the Internet</a>. 
      </p>
    </div>
    <h3>Materials</h3>
    <ul>
    <li><a href="https://docs.google.com/presentation/d/1O4fSXY7KwHj-e6LcU6_q4sx7yuY_Epad2rXuCBxGwnk/edit?ts=5f6b40b2#slide=id.p5" target="_blank" title="">Slides</a></li>
    <li>Videos.  There are four video clips embedded in this lesson: </li><ul><li>Video 1: CS Unplugged Double-locked box (4:22)</li><li>Video 2: Diffie-Hellman Key Exchange (4:21)</li><li>Video 3: RSA Public Key Encryption (3:59)</li><li>Video 4: Securing
        the Internet (6:59). 
    </li></ul></ul>
    

Learning Activities
--------------------

.. raw:: html

    <p>
    <h3 id="est-length">Estimated Length: 45 minutes</h3>
    <ul>
    <li><b>Hook/Motivation (10 minutes):</b> Show Video 1 (4:22), the CS Unplugged 
         <a href="http://www.youtube.com/watch?feature=player_embedded&amp;v=jJrICB_HvuI" target="_blank">video</a> 
         — locking a box with 
         two keys is an analogy for the public key encryption.  This video  illustrates 
         the key exchange problem. (<a href="http://csunplugged.org/public-key-encryption" target="_blank">More info</a>)
      </li>
    <li><b>Experiences and Explorations (25 minutes)</b>
    <ul>
    <li><b>Discussion:</b> Discuss how the key exchange problem, if left unsolved, would make it 
            impossible (or at least very impractical) to have secure transactions on the Internet.
          </li>
    <li><b>Presentation 1: Diffie-Hellman:</b> Using the slides or Video 2 (4:21) discuss with
            the students the Diffie-Hellman solution to the key exchange problem.  The slides and video include a
            <a href="https://youtu.be/YEBfamv-_do" target="_blank">Brit Cruise video</a> that describes
            Diffie-Hellman in terms of a paint-mixing analogy, which nicely illustrates the concept of a
            one-way function -- in this case, mixing paint is easy but unmixing it is hard.  Emphasize that
            Diffie-Hellman uses an <i><b>intractable mathematical problem</b></i> (analogous to unmixing paint), 
            to protect the exchange of a secret key.
            <p>Let students experiment with 
              <a href="http://appinventor.cs.trincoll.edu/csp/diffiehellmancolor/" target="_blank">this embedded color-mixing activity</a>, which in addition to illustrating the
              paint-mixing analogy, also gives them another experience with hexadecimal numbers. 
            </p>
    </li>
    <li><b>Discussion:</b> Discuss the color-mixing analogy, emphasizing  that
            Diffie-Hellman uses an <i><b>intractable mathematical problem</b></i> 
            (analogous to unmixing paint), to protect the exchange of a secret key.
          </li>
    <li><b>Presentation 2: RSA Public Key Encryption:</b> Using the slides or Video 3 (3:59) review RSA and emphasize how it solves the efficiency problem with the Diffie-Helman key exchange.
          </li><li><b>Presentation 3: Securing the Internet: </b>Using the slides or Video 4 (6:59) review how the modern cryptographic techniques work together to secure the Internet. Discuss what the 's' in https stands for and how certificates work.</li>
    </ul>
    </li>
    <li><b>Rethink, Reflect and/or Revise (10 minutes):</b> Review public key 
        cryptography and the idea that two keys (public and private) should be used. 
        Have students complete the portfolio reflection questions.
      </li>
    </ul>
    <div id="accordion">
    <h3 class="ap-classroom">AP Classroom</h3>
    <div class="yui-wk-div">
    <p>The College Board's <a href="http://myap.collegeboard.org" target="_blank" title="AP Classroom Site">AP Classroom</a> provides a question bank and Topic Questions. You may create a formative assessment quiz in AP Classroom, assign the quiz (a set of questions), and then review the results in class to identify and address any student misunderstandings. The following are suggested topic questions that you could assign once students have completed this lesson.</p>
    <p><b>Suggested Topic Questions:</b></p>
    </div>
    <h3 class="assessment">Assessment Opportunities</h3>
    <div>
    <p><b>Solutions:</b></p>
    <ul>
    <li>Note: Solutions are only available to verified educators who have joined the <a href="./unit?unit=1&amp;lesson=39" target="_blank">Teaching Mobile CSP Google group/forum in Unit 1</a>.</li>
    <li><a href="https://drive.google.com/open?id=1Us4_AJcI_9Xja_1lTTr6RJmI3Ko57W4Kisv7hmXv5cw" target="_blank">Quizly Solutions</a>
    </li>
    <li><a href="https://sites.google.com/a/css.edu/jrosato-cis-1001/" target="_blank">Portfolio Reflection Questions Solutions</a>
    </li>
    </ul>
    </div>
    <h3 class="diff-practice">Differentiation: More Practice</h3>
    <div>
    <p>If students are struggling with lesson concepts, have them review the following resources:</p>
    <ul>
    <li><a href="https://www.khanacademy.org/computing/computer-science/cryptography" target="_blank">Khan Academy Cryptography videos</a></li>
    <li><a href="https://britcruise.com/2012/02/14/2000-years-of-cryptography-in-8-5min/" target="_blank">Brit Cruise videos</a></li>
    </ul>
    </div>
    <h3 class="diff-enrich">Differentiation: Enrichment</h3>
    <div>
    <p>Have students bring in a current events article related to cryptography to share with the class.</p>
    </div>
    <h3 class="bk-knowledge">Background Knowledge: Certificate Authorities</h3>
    <div class="yui-wk-div">
    <p>This WhatIs.com entry on <a href="http://searchsecurity.techtarget.com/definition/certificate-authority" target="_blank">Certificate Authorities</a> provides a good background on how public keys are issued. The image below might also be helpful in 
          understanding the relationship between the systems.</p>
    <img alt="Alice and Bob's public key come from the certificate authority" src="https://www.comodo.com/images/support/certs7.gif"/>
    </div>
    </div> <!-- accordion -->
    <div class="pd yui-wk-div">
    

Professional Development Reflection
------------------------------------

.. raw:: html

    <p>
    <p>Discuss the following questions with other teachers in your professional development program.</p>
    <ul>
    <li>How does the lesson reinforce the enduring understanding that cybersecurity is an important concern for the Internet? What other connections or examples would be relevant for students?</li> <!-- for an EU -->
    </ul>
    <!-- These are the PD exit slips.  We should have corresponding exit slips for use after the classroom lesson. -->
    
.. poll:: mcsp-6-7-1
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


    
.. fillintheblank:: mcsp-6-7-2

    What questions do you still have about the lesson or the content presented? |blank|

    - :/.*/i: Thank you. We will review these to improve the course.
      :x: Thank you. We will review these to improve the course.


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    </div></div>
    </div>