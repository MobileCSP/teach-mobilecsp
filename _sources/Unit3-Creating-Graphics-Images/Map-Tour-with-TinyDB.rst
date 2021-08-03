.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Map Tour with TinyDB
====================

.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
      $(document).ready(function() {
          generateFrameworkTable(EKmapping['3.09']);
          generateHovers();
      });
    
    </script>
    <p class="overview"><a href="https://runestone.academy/runestone/books/published/mobilecsp/Unit3-Creating-Graphics-Images/Map-Tour-With-TinyDB.html" target="_blank" title="">This lesson</a> introduces the concept of <i>persistent storage</i> in apps by storing the destinations lists in the Map Tour app in a database called TinyDB, so that it is remembered from the last run of the app. It reinforces the enduring understanding that there are trade-offs in representing digital data, in this case, the differences between storing data in memory (variables) versus persistently (TinyDB).</p>
    <table border="" class="framework" id="genTable" width="100%"></table>
    <div class="pd yui-wk-div">
    <h3>Professional Development</h3>
    <p><b>The Student Lesson:</b> Complete the activities for 
        <a href="https://runestone.academy/runestone/books/published/mobilecsp/Unit3-Creating-Graphics-Images/Map-Tour-With-TinyDB.html" target="_blank" title="">Mobile CSP Unit 3 Lesson 3.9: Map Tour with TinyDB </a>.
      </p>
    </div>
    <h3>Materials</h3>
    <ul><li>Presentation system (LCD projector/Interactive whiteboard)</li><li>Access to computer, laptop, or Chromebook (install the Companion app on Chromebooks)</li><li>Access to mobile device with the Companion app installed or access to the emulator installed on the computer or laptop. </li><li>Map Tour with TinyDB Tutorial (video or handout)</li></ul>
    

Learning Activities
--------------------

.. raw:: html

    <p>
    <h3 id="est-length">Estimated Length: 45 minutes</h3>
    <ul>
    <li><b>Hook/Motivation (5 minutes):</b> Ask students how does Amazon know your name when you go to amazon.com? How does it remember all your previous orders? Where is this information stored? See if they have heard of a database. Remind students of the use of variables and properties in the Map Tour app. Ask them what the value of the variable is each time the app is re-started or the properties of the UI components. Explanation: Each time the app is started, the variables and properties are set to their initial values the programmer set up in the app. Right now, it does not remember information from the last time the app was used. In this lesson, we will learn how to make data <i>persist</i>, or last, when an app is closed and restarted.</li>
    <li><b>Experiences and Exploration (30 minutes):</b>
    <ul>
    <li><b>Presentation (5 minutes):</b> Give students an overview of the TinyDb component using the video or 
            <a href="https://docs.google.com/presentation/d/11OONNUVv5ETqBUwaCofR4a_xDF-1fdLGSnpHLHq-smw" target="_blank">slides.</a>
    </li>
    <li><b>Tutorial Walkthrough (15 minutes):</b> Lead students through incorporating the TinyDb component into the MapTour app so that it will save the list of destinations for the next time the app is used. Make sure that they stop after adding a location and try restarting their app and they will notice that the saved location is gone. This is motivation for adding persistent database storage.</li>
    <li><b>Extensions (15 minutes):</b> Working in pairs, students should attempt the extensions. For advanced students who want to explore the special Any Component blocks, see the enrichment section below.</li>
    </ul>
    </li>
    <li><b>Rethink, Reflect, and Revise (5 minutes):</b> Review the concept of persistent data and the TinyDB component. How did it and the creative projects enhance the usability of the app by storing data? Students should complete the interactive exercises and portfolio reflection questions.</li>
    </ul>
    <div class="ui-accordion ui-widget ui-helper-reset yui-wk-div" id="accordion" role="tablist">
    <h3 class="ap-classroom">AP Classroom</h3>
    <div class="yui-wk-div">
    <p>The College Board's <a href="http://myap.collegeboard.org" target="_blank" title="AP Classroom Site">AP Classroom</a> provides a question bank and Topic Questions. You may create a formative assessment quiz in AP Classroom, assign the quiz (a set of questions), and then review the results in class to identify and address any student misunderstandings.The following are suggested topic questions that you could assign once students have completed this lesson.</p>
    <p><b>Suggested Topic Questions:</b></p><br/><ul><li><span style="font-weight: normal;">Topic 3.2 Data Abstraction</span><br/></li><li><span style="font-weight: 400;">Topic 3.10 Lists</span><br/></li></ul></h4>
    </div>
    <h3 aria-controls="ui-id-2" aria-expanded="false" aria-selected="false" class="assessment ui-accordion-header ui-state-default ui-corner-all" id="ui-id-1" role="tab" tabindex="0">Assessment Opportunities and Solutions</h3>
    <div aria-hidden="true" aria-labelledby="ui-id-1" class="ui-accordion-content ui-helper-reset ui-widget-content ui-corner-bottom yui-wk-div" id="ui-id-2" role="tabpanel" style="display: none;">
    <p><b>Solutions:</b></p>
    <ul>
    <li>Note: Solutions are only available to verified educators who have joined the <a href="./unit?unit=1&amp;lesson=39" target="_blank">Teaching Mobile CSP Google group/forum in Unit 1</a>.</li>
    <li><a href="https://drive.google.com/open?id=1g87RA0YQaumslPzsNQpk-oZ-KLn-Rdy1" target="_blank">Map Tour with Tiny DB without enhancements .aia file</a>
    </li>
    <li><a href="https://docs.google.com/document/d/1jl2wcNNu63tUjMQ2KimUuMbqLnSYO3FqenuLrRVPj3Q/edit?usp=sharing" target="_blank">Map Tour with Tiny DB Enhancement Solutions </a>
    </li>
    <li><a href="https://drive.google.com/open?id=1Y0SK0Tpi8HawdBw10UwqzvQGKHPrjzV8" target="_blank">Map Tour with Tiny DB Enhancements .aia file </a>
    </li>
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
    <h3 aria-controls="ui-id-4" aria-expanded="false" aria-selected="false" class="diff-practice ui-accordion-header ui-state-default ui-corner-all" id="ui-id-3" role="tab" tabindex="-1">Differentiation: More Practice</h3>
    <div aria-hidden="true" aria-labelledby="ui-id-3" class="ui-accordion-content ui-helper-reset ui-widget-content ui-corner-bottom yui-wk-div" id="ui-id-4" role="tabpanel" style="display: none;">
    <p>Have students review the mini-lessons on data persistence on AppInventor.org: <a href="http://www.appinventor.org/content/howDoYou/persistence" target="_blank">How Do You? Store Data Persistently</a></p>
    </div>
    <h3 aria-controls="ui-id-6" aria-expanded="false" aria-selected="false" class="diff-enrich ui-accordion-header ui-state-default ui-corner-all" id="ui-id-5" role="tab" tabindex="-1">Differentiation: Enrichment</h3>
    <div aria-hidden="true" aria-labelledby="ui-id-5" class="ui-accordion-content ui-helper-reset ui-widget-content ui-corner-bottom yui-wk-div" id="ui-id-6" role="tabpanel" style="display: none;">
    <ul>
    <li><b>Optional extension (hard) - New Markers using Any Component blocks:</b> When the user adds a destination to the map tour, your app could also add a marker at that location. This is a little challenging. Follow the algorithm below:
    <ul><li>Add a new variable newMarker set to empty text string "".
      </li><li>In When Map.LongPressAtPoint, set the newMarker to Map.CreateMarker at the pressed latitude and longitude.
     </li><li>In Notifier.AfterTextInput, we can set the marker’s title to the user’s response. Since this is a new marker added in the code, we do not have a Marker in the UI to use for the set block.  At the bottom of the blocks drawers on the left, there is a section called <b>Any Components</b>, where you can get or set a property of any components of a certain type instead of specific ones in your UI. Find the green Marker.Title of component block and the Marker.EnableInfoBox of Component block under Any Components at the bottom left of the screen. Put the get newMarker variable block into the ofComponent slots of these blocks. The title should be set to the user’s response and Enable InfoBox should be set to true (in  the Logic drawer).
     </li></ul>
        Note that the new markers will not be regenerate when you re-start the app. It is possible to write code with a loop to do this from the list of destinationsLatLong, but it is too complex for Unit 3.
    </li>
    <li><b>Optional extension (Any Component Blocks):</b>Add a TextToSpeech component to the UI. Use the when Map.FeatureClick event handler. When any feature is clicked on the map (this includes all markers), call TextToSpeech and speak the Marker.Title of that feature. Hint: to do this, you will need to use the Marker.Title of component block under Any Components at the bottom left of the screen.</li>
    <li>Students could also explore using the TinyDb component to store the last GPS location.</li></ul>
    </div>
    <h3 aria-controls="ui-id-8" aria-expanded="false" aria-selected="false" class="bk-knowledge ui-accordion-header ui-state-default ui-corner-all" id="ui-id-7" role="tab" tabindex="-1">Background Knowledge: TinyDB</h3>
    <div aria-hidden="true" aria-labelledby="ui-id-7" class="ui-accordion-content ui-helper-reset ui-widget-content ui-corner-bottom yui-wk-div" id="ui-id-8" role="tabpanel" style="display: none;">
    <p>TinyDB only stores data on the device, which is cost efficient, but doesn't allow sharing of data between devices. Also, the size and the amount of data that can be stored will be limited with a TinyDB. This should lead into the topic of a TinyWebDB in an upcoming lesson, which allows for the sharing of data via the web.</p>
    <p><a href="http://ai2.appinventor.mit.edu/reference/components/storage.html#TinyDB" target="_blank">AI2 Documentation on Tiny DB</a></p>
    </div>
    </div> <!-- accordion -->
    <div class="pd yui-wk-div">
    

Professional Development Reflection
------------------------------------

.. raw:: html

    <p>
    <p>Discuss the following questions with other teachers in your professional development program.</p>
    <ul>
    <li>How does this lesson address the learning objective of extracting information from data using a program? <div class="hover ctp yui-wk-div" data-id="DAT-2.D">[LO DAT-2.D]</div></li>
    </ul>
    <!-- These are the PD exit slips.  We should have corresponding exit slips for use after the classroom lesson. -->
    
.. poll:: mcsp-3-9-1
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


    
.. fillintheblank:: mcsp-3-9-2

    What questions do you still have about the lesson or the content presented? |blank|

    - :/.*/i: Thank you. We will review these to improve the course.
      :x: Thank you. We will review these to improve the course.


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    </div>
    </div>