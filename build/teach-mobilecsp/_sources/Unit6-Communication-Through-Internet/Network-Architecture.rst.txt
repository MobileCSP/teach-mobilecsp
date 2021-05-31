.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Network Architecture
====================

.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
     $(document).ready(function() {
          generateFrameworkTable(EKmapping['6.03']);
          generateHovers();
      }); 
    
    </script>
    <p class="overview"><a href="https://course.mobilecsp.org/mobilecsp/unit?unit=25&amp;lesson=102" target="_blank" title="">This lesson</a> 
      dives deeper into how the Internet works, exploring the addressing system used to send data. Students watch 
      a series of lectures and use several networking tools, such as <i>ping</i> and <i>traceroute</i> to observe 
      the workings  of the Internet. </p>
    <table border="" class="framework" id="genTable" width="100%"></table>
    <div class="pd yui-wk-div">
    <h3>Professional Development</h3>
    <p><b>The Student Lesson:</b> Complete the activities for <a href="https://course.mobilecsp.org/mobilecsp/unit?unit=25&amp;lesson=102" target="_blank" title="">Mobile CSP Unit 6: Lesson 6.3 Network Architecture</a>.
      </p>
    </div>
    <h3>Materials</h3>
    <ul>
    <li>Computer lab with projection system</li>
    <li><a href="https://docs.google.com/presentation/d/1g7NmzbMvyBYLZwe2NtWXSurW4D7o-uCKYCdI2yvDFIc" target="_blank" title="">Slides</a> :
         This is slide deck contains 60 slides) and is broken into two parts, with corresponding videos, for this lesson.  
         It is meant to be interspersed with two hands-on POGIL activities. 
      </li>
    <li>Videos, embedded in student lesson.  There are 2 videos:  Video 1 (7:47) and Video 2 (7:15).
      </li>
    <li><a href="https://docs.google.com/document/d/1vCMjrLWMzU-bs1zv8Btu-rjrcvzQ21J0HarznLgL30g/edit?usp=sharing" target="_blank">Printouts for TCP/IP Packet Routing Activity</a> for each group of 4 in the class and <b>scissors</b> needed to cut out packets in page 3. Or use this new <a href="https://docs.google.com/presentation/d/145iS_7CrMP8n9uek7EX7uvfjjIBKsdhj0JHpuQelp1s/edit?usp=sharing" target="_blank">synchronous online version of the packet routing activity with editable slides</a> - do File/Make a Copy and change the Share permissions to anyone can edit.</li>
    </ul>
    

Learning Activities
--------------------

.. raw:: html

    <p>
    <h3 id="est-length">Estimated Length: 90 minutes</h3>
    <ul>
    <li><b>Hook/Motivation (10 minutes):</b>  Ask the students: You are at home writing an e-mail to a friend 
         who is at their home. When you press 'Send', how does the e-mail get to your friend's computer? Show this short video called <a href="https://www.youtube.com/watch?v=ewrBalT_eBM" target="_blank">A Packet's Tale</a>.
         <b>Explanation:</b> Explain that information is sent in packets over the Internet, between 
         servers, from one IP address to another. You may want to assign <a href="https://www.youtube.com/watch?v=PBWhzz_Gn10" target="_blank">this longer video about packets traveling through the internet</a> from the still curious section as a homework assignment the night before class.
      </li>
    <li><b>Experiences and Explorations (70 minutes):</b>
    <ul>
    <li><b>Lecture, Part 1:</b> Video 1 (slides 1-37, video 7:47) focuses on basic Internet 
            architecture and introduces the concept of packet switching. It explains the motivation
            behind the Internet's decentralized, redundant architecture, where messages are divided
            into small packets that are routed independently from host to host. The lecture/video
            contains two possible pause points, one that uses the <i>ping</i> utility to test the
            reachability of a host on the internet, and a second point that uses the <i>traceroute</i>
            utility to trace the routing of packets.  Breaking up the video to try these utilities
            will be good preparation for the following POGIL activity. 
          </li>
    <li><b>POGIL Activity 1 (20 minutes) -  Using Ping and Traceroute to Investigate the Internet</b> (15 minutes).
            The video ends with the following question -- <i>Does the geographical location of hosts
            on the Internet affect latency</i> -- in other words, do messages take longer to reach hosts
            that are farther away geographically?  Students are asked to use the ping and traceroute 
            utilities to explore this question.  <b>Answer: </b> All things being equal, the further 
            messages have to travel, the longer it should take.  However, not all things are equal. There
            are different types of channels over which the packets get routed, some faster than others.
            More importantly, the routes will take a number of hops -- the more hops, typically, the 
            more latency.  
          </li>
    <li><b>Lecture, Part 2:</b> The second video (slides 38-60, video 7:18) focuses on the Internet's
            abstraction hierarchy and shows, through the example of a web page request, how the different
            protocols work together to route the message's packets from source to destination. It describes
            the TCP/IP protocol, emphasizing the different roles they play in the message routing. 
          </li>
    <li><b>POGIL Activity 2 -  TCP/IP Packet Routing </b> (30 minutes). This hands-on activity asks
            students to play the roles of the different abstraction layers.  POGIL teams of 4 broken into
            application layer, transmission layer, internet layer, and link layer. As teacher you will create
            a <i><b>routing table</b></i>, that students will use to distribute messages (on paper) from one
            classmate in one POGIL group to another classmate in a different POGIL group.  The activity closely
            mirrors the Internet abstraction hierarchy. The activity should progress as follows:
            <ul>
    <li>Print out  <a href="https://docs.google.com/document/d/1vCMjrLWMzU-bs1zv8Btu-rjrcvzQ21J0HarznLgL30g/edit?usp=sharing" target="_blank">Packet Switching Activity handouts</a> for each team of 4 in your class and provide scissors or cut out the packets on page 3.  </li>
    <li>Or use this new <a href="https://docs.google.com/presentation/d/145iS_7CrMP8n9uek7EX7uvfjjIBKsdhj0JHpuQelp1s/edit?usp=sharing" target="_blank">synchronous online version of the packet routing activity with editable slides</a> - do File/Make a Copy and change the Share permissions to anyone can edit.
                <p>Here is a video of a Mobile CSP teacher, Deddie Quillen, setting up the handouts for her class:<br/><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" frameborder="0" height="315" src="https://www.youtube-nocookie.com/embed/VYv_pKhaKYc?rel=0" width="560"></iframe></p></li>
    <li>Ask or assign students into teams of 4. Show the routing table on page 1 of the handout on the projector or board and assign an IP address to each group which they should write down on their handouts. Or you could prepare this in advance and write the assigned IP addresses and group leaders on the handouts you give out as in the video above.</li>
    <li>This activity works best with the teacher as the conductor leading the class through each step. Direct the teams through the activity: 
                  <ol>
    <li>First have the application layer student in each team write a message (try to make sure each team will receive a message by telling them who to write the message to);</li>
    <li>Then have the transport layer student break the message into packets,</li>
    <li>Then have the internet layer add the IP addresses,</li>
    <li>Then have the link layer pass the packets to another group. Have them mix them up and pass different packets to different groups (the packets take different routes through the network). </li>
    <li>When a group receives a packet they should pass it back up through the layers and follow the directions until they receive their complete message. If the internet layer realizes that the packet is not for them, s/he should pass it back down to the link layer to give to another group.</li>
    <li>After each team sends and receives a message, have them discuss the discussion questions in their groups and then as a class. </li>
    </ol>
    <b>Answers:</b>
    <ol>
    <li><b>Packet Order:</b> the order of the packets does not matter since the TCP header will tell you how to order them, e.g. packet 2 of 3.</li>
    <li><b>Missing Packets:</b> You could steal one of the packets during the activity to see what happens. If there is a missing packet, the TCP layer will know which packet is missing from the TCP headers, e.g. packet 2 of 3. A message needs to be sent to the sender to let them know that a packet is missing and to ask the sender to send it again. For this, we would need a sender IP address in the IP header as well as the recipient's IP address. Packets in real life contain both addresses in the IP header.</li>
    <li><b>Corrupted Packets:</b> How do you know you got the right data? Usually packets have a checksum (or parity bits) to check that you got all the bits. </li>
    <li><b>Security/Privacy:</b> In this simulation, it would be very easy to read everyone's messages. There's no security or privacy. <b>Packet sniffers</b> in real life can capture packets in a network and read them unless they are encrypted. You will probably need to introduce the terms encryption and packet sniffers to the class.</li>
    </ol>
    </li>
    </ul>
    </li></ul>
    </li>
    <li><b>Rethink, Reflect and/or Revise (10 minutes):</b> Review how the Internet works, 
        including the important terms covered in the videos. Students should complete a 
        reflection on their portfolio based on the POGIL activities and complete the interactive exercises.
      </li>
    </ul>
    <div class="yui-wk-div" id="accordion">
    <h3 class="ap-classroom">AP Classroom</h3>
    <div class="yui-wk-div">
    <p>The College Board's <a href="http://myap.collegeboard.org" target="_blank" title="AP Classroom Site">AP Classroom</a> provides a question bank and Topic Questions. You may create a formative assessment quiz in AP Classroom, assign the quiz (a set of questions), and then review the results in class to identify and address any student misunderstandings.The following are suggested topic questions that you could assign once students have completed this lesson.</p>
    <h4>Suggested Topic Questions:</h4>
    <ul>
    <li>Topic 4.1 The Internet</li>
    <li>Topic 4.2 Fault Tolerance</li>
    </ul>
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
    <p>If students are struggling with lesson concepts, have them review the following resources:</p>
    <ul>
    <li><a href="http://www.internetsociety.org/internet" rel="nofollow" target="_blank">Internet FAQ</a> — the Internet Society's page provides concise answers to frequently asked questions about the Internet, including what it is and how it works.</li>
    <li>Watch <a href="https://www.youtube.com/watch?v=PBWhzz_Gn10" target="_blank">Warriors of the Net</a>, a classic 12 minute animated video about packets traveling through the Internet.</li>
    </ul>
    </div>
    <h3 class="bk-knowledge">Background Knowledge</h3>
    <div class="yui-wk-div">
    <ul>
    <li><a href="http://www.internetsociety.org/internet" rel="nofollow" target="_blank">Internet FAQ</a> — the Internet Society's page provides concise answers to frequently asked questions about the Internet, including what it is and how it works.</li>
    <li><a href="http://www.stanford.edu/class/msande91si/www-spr04/readings/week1/InternetWhitepaper.htm" rel="nofollow" target="_blank">Whitepaper</a> — a fairly concise but authoritative explanation of Internet infrastructure. </li>
    <li><a href="http://en.wikipedia.org/wiki/Internet" rel="nofollow" target="_blank">Wikipedia</a> — an authoritative and comprehensive resource with around 90 references to original sources.</li>
    <li>Watch <a href="https://www.youtube.com/watch?v=PBWhzz_Gn10" target="_blank">Warriors of the Net</a>, a classic 12 minute animated video about packets traveling through the Internet.</li>
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
    <li>Explain how the various levels of abstraction influence characteristics of the Internet? This really combines two of the courses big ideas: abstraction and the Internet. <div class="hover eu yui-wk-div" data-id="6.1">[EU 6.1]</div></li> <!-- for an EU -->
    </ul>
    <!-- These are the PD exit slips.  We should have corresponding exit slips for use after the classroom lesson. -->
    
.. mchoice:: mcsp-6-3-1
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


    
.. fillintheblank:: mcsp-6-3-2

    What questions do you still have about the lesson or the content presented? |blank|

    - :/.*/i: Thank you. We will review these to improve the course.
      :x: Thank you. We will review these to improve the course.


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    </div>
    </div>