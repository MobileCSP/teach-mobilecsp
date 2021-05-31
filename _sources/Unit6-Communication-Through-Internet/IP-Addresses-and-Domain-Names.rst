.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

IP Addresses and Domain Names
=============================

.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
     $(document).ready(function() {
          generateFrameworkTable(EKmapping['6.04']);
          generateHovers();
      }); 
    
    </script>
    <p class="overview"><a href="https://course.mobilecsp.org/mobilecsp/unit?unit=25&amp;lesson=190" target="_blank" title="">This lesson</a> has students use a DNS simulator app to send messages to other clients on a router. They learn about DNS, IP addresses, and packets. </p>
    <table border="" class="framework" id="genTable" width="100%"></table>
    <div class="pd yui-wk-div">
    <h3>Professional Development</h3>
    <p><b>The Student Lesson:</b> Complete the activities for <a href="https://course.mobilecsp.org/mobilecsp/unit?unit=25&amp;lesson=190" target="_blank" title="">Mobile CSP Unit 6: Lesson 6.4 IP Addresses and Domain Names</a>.
      </p>
    </div>
    <h3>Materials</h3>
    <ul>
    <li>Computer lab with projection system</li><li><a href="https://docs.google.com/presentation/d/1S9SA6Y_SUU7o0oAbj7cpt7DGO5hgzJf7p3_vHWnCRG0/edit#slide=id.g341a98a4a_031" style="color: rgb(120, 71, 178);" target="_blank" title="">Slides</a></li>
    <li>Tablets </li>
    </ul>
    

Learning Activities
--------------------

.. raw:: html

    <p>
    <h3 id="est-length">Estimated Length: 45 minutes</h3>
    <ul>
    <li><b>Hook/Motivation (5 minutes):</b>
    </li>
    <li><b>Experiences and Explorations (35 minutes):</b>
    <ul>
    <li><b>Lecture</b> Video (7:55) and slides  describe the how the IP 
            address system and the Domain Name System work together to identify data and 
            network locations.
          </li>
    <li>
    <b>DNS Network Simulation Activities</b> allow students to explore how the DNS provides look-up services to translate hostnames (login IDs) to IP addresses and how IP addresses can be used to communicate between hostnames.
            <br/>
    <b>The teacher needs to run the DNS simulator app first and push the NEW CLASS CODE button and write this class code on the board so that all the students can enter that class code in their apps. This will ensure that they can see each other on the simulated network.</b>
    <br/> </li>
    <li>
    <b>POGIL Activity</b> allows students to explore how to enhance the widget to handle multiple messages. <br/>
    <b>        Solution:</b>
    <table border="">
    <tbody><tr><th>Recipient</th><th>Sender#</th></tr>
    <tr><td>
    <pre>mailbox ← empty list
    Repeat every 3 seconds
    {
       Repeat until mailbox is empty list
       {
           Remove_msg_at_front_of_list 
       }   
    }   
        
    </pre>
    </td><td>
               recipient's mailbox ← Insert_at_end_of_list("sender#: <em>ip address </em>: <em>message</em> ")
                </td></tr><tr>
    </tr></tbody></table><br/>
            Students could also use Insert_at_end and Remove_at_end 
            This strategy is a  <b>First In First Out (FIFO)</b> approach which turns the list into a  data structure called a <b>queue</b> in comparison to a <b>Last In First Out (LIFO)</b> approach for a <b>stack</b>. Students do not need to know these data structures, but you can talk about whether a FIFO and LIFO approach is necessary for the queueing of messages. Some examples of FIFO in real life are waiting in lines at the bank, cashier, kiosk, bus, etc., as well as sending a document to the printer where it waits in a FIFO printer queue to be processed.
    
         </li>
    </ul>
    </li>
    <li><b>Rethink, Reflect and/or Revise (5 minutes):</b> Review how the Internet works, 
        including the important terms covered in the videos. Students should complete a 
        reflection on their portfolio based on the activities (this may be assigned for homework), 
        and complete the interactive exercises.
      </li>
    </ul>
    <div class="yui-wk-div" id="accordion">
    <h3 class="ap-classroom">AP Classroom</h3>
    <div class="yui-wk-div">
    <p>The College Board's <a href="http://myap.collegeboard.org" target="_blank" title="AP Classroom Site">AP Classroom</a> provides a question bank and Topic Questions. You may create a formative assessment quiz in AP Classroom, assign the quiz (a set of questions), and then review the results in class to identify and address any student misunderstandings.The following are suggested topic questions that you could assign once students have completed this lesson.</p>
    <h4>Suggested Topic Questions:</h4>
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
    <ul>
    <li>DNS Network Simulation</li>
    <li>Modification of Protocol to Handle Multiple Messages</li>
    <li>Modification of Protocol to Break Messages into Multiple Packets</li>
    </ul>
    <li><i><b>Portfolio Reflections:</b></i>
    <ul>
    <li>LO 5.2.1 - Students should be able to explain how programs implement algorithms. Students are given practice on this skill with the POGIL exercises.</li>
    <li>LO 6.1.1 - Students should be able to explain the abstractions in the Internet and how the Internet functions. Use of the DNS simulator allows students to learn how DNS works on the Internet.</li>
    <li>LO 6.2.1 - Students should be able to explain the characteristics of the Internet and the systems build on it. The DNS is a key component in the infrastructure of the Internet.</li>
    <li>LO 6.2.2 - Students should be able to explain how the characteristics of the Internet influence the systems built on it. Routing and address are key components to a distributed system such as the Internet.</li>
    </ul>
    </li>
    <li><i><b>In the DNS Simulation, look for:</b></i> students ablity to ask the DNS for the IP addresses of other login IDs on the system. Also look for message exchanges between the student and the Amazon BOT as well as between students and their peers. 
          </li>
    </ul>
    </div>
    <h3 class="diff-practice">Differentiation: More Practice</h3>
    <div class="yui-wk-div">
    <p>If students are struggling with lesson concepts, have them review the following resources:</p>
    <ul>
    <li><a href="http://www.internetsociety.org/internet" rel="nofollow" target="_blank">Internet FAQ</a> — the Internet Society's page provides concise answers to frequently asked questions about the Internet, including what it is and how it works.</li>
    </ul>
    </div>
    <h3 class="bk-knowledge">Background Knowledge</h3>
    <div class="yui-wk-div">
    <ul>
    <li><a href="http://www.internetsociety.org/internet" rel="nofollow" target="_blank">Internet FAQ</a> — the Internet Society's page provides concise answers to frequently asked questions about the Internet, including what it is and how it works.</li>
    <li><a href="http://www.stanford.edu/class/msande91si/www-spr04/readings/week1/InternetWhitepaper.htm" rel="nofollow" target="_blank">Whitepaper</a> — a fairly concise but authoritative explanation of Internet infrastructure. </li>
    <li><a href="http://en.wikipedia.org/wiki/Internet" rel="nofollow" target="_blank">Wikipedia</a> — an authoritative and comprehensive resource with around 90 references to original sources.</li>
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
    </ul>
    <!-- These are the PD exit slips.  We should have corresponding exit slips for use after the classroom lesson. -->
    
.. mchoice:: mcsp-6-4-1
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


    
.. fillintheblank:: mcsp-6-4-2

    What questions do you still have about the lesson or the content presented? |blank|

    - :/.*/i: Thank you. We will review these to improve the course.
      :x: Thank you. We will review these to improve the course.


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    </div>
    </div>