.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Persisting Photos Tutorial and Projects (Optional)
==================================================

.. raw:: html

	<!-- Copy these lines to the top of the lesson's HTML code.  -->
	<script type="text/javascript" src="https://code.jquery.com/jquery-1.11.3.min.js"></script>
	<script type="text/javascript" src="assets/lib/lessons/tipped.js"></script>
	<script type="text/javascript" src="assets/lib/Framework2020.js"></script>
	<link rel="stylesheet" href="//code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css">
	<link rel="stylesheet" type="text/css" href="assets/lib/lessons/tipped.css">
	<link rel="stylesheet" type="text/css" href="assets/lib/lessons/lessons.css">
	<script src="//code.jquery.com/ui/1.11.4/jquery-ui.js"></script>
	<script>
	$(document).ready(function() {
	     generateFrameworkTable(EKmapping['9.06']);
	     generateHovers();
	 }); 
	
	</script>
	
	<p class="overview"><a target="_blank" href="https://runestone.academy/runestone/books/published/mobilecsp/Unit9-Beyond-AP/Persisting-Photos-Tutorial.html" title="">This lesson</a> introduces the concept of <i>persistent storage</i> in apps by adding a way to save pictures in the Paint Pot app. It reinforces the enduring understanding that there are trade-offs in representing digital data, in this case, the differences between storing data in memory (variables) versus persistently (TinyDB).</p>
	
	<table border id="genTable" class="framework" width="100%"></table>
	
	<div class="pd yui-wk-div">
	 <h3>Professional Development</h3> 
	 <p><b>The Student Lesson:</b> Complete the activities for 
	   <a href="https://runestone.academy/runestone/books/published/mobilecsp/Unit9-Beyond-AP/Persisting-Photos-Tutorial.html" target="_blank" title="">Mobile CSP Lesson 9.6: Persisting Photos Tutorial</a>.
	 </p>
	</div>
	
	
	<h3>Materials</h3>
	<p>Android devices or emulator</p>
	
	
Learning Activities
-----------------------

.. raw:: html

	<h3 id="est-length">Estimated Length: 90 minutes</h3>
	<p></p>
	<ul>
	 <li><b>Hook/Motivation (5 minutes):</b> Remind students of the use of variables and properties in the Paint Pot app. Ask them what the value of the variable is each time the app is re-started or the properties of the UI components. Explanation: Each time the app is started, the variables and properties are set to their initial values the programmer set up in the app. Right now, it does not remember information from the last time the app was used. In this lesson, we will learn how to make data <i>persist</i>, or last, when an app is closed and restarted.</li>
	 <li><b>Experiences and Exploration (30 minutes):</b> 
	   <ul>
	     <li><b>Presentation (5 minutes):</b> Give students an overview of the TinyDb component using the video or 
	       <a target="_blank" href="https://docs.google.com/presentation/d/11OONNUVv5ETqBUwaCofR4a_xDF-1fdLGSnpHLHq-smw">slides.</a>
	     </li>
	     <li><b>Tutorial Walkthrough (10 minutes):</b> Lead students through incorporating the TinyDb component into the Paint Pot app so that it will save the background image information for the next time the app is used.</li>
	     <li><b>Creative Mini Projects (15 minutes):</b> Working in pairs, students should attempt the mini projects incorporating lists of the images taken and adding a ListPicker.</li>
	   </ul>
	 </li>
	 <li><b>Rethink, Reflect, and Revise (10 minutes):</b> Review the concept of persistent data and the TinyDB component. How did it and the creative projects enhance the usability of the app by storing data? Students should complete the interactive exercises and portfolio reflection questions.</li>
	</ul>
	
	
	<div id="accordion" class="ui-accordion ui-widget ui-helper-reset yui-wk-div" role="tablist">
	<h3 class="ap-classroom">AP Classroom</h3>
	 <div class="yui-wk-div">
	 <p>The College Board's <a href="http://myap.collegeboard.org" target="_blank" title="AP Classroom Site">AP Classroom</a> provides a question bank and Topic Questions. You may create a formative assessment quiz in AP Classroom, assign the quiz (a set of questions), and then review the results in class to identify and address any student misunderstandings.The following are suggested topic questions that you could assign once students have completed this lesson.</p>
	   <h4>Suggested Topic Questions:</h4>
	</div>
	<h3 class="assessment ui-accordion-header ui-state-default ui-corner-all" role="tab" id="ui-id-1" aria-controls="ui-id-2" aria-selected="false" aria-expanded="false" tabindex="0">Assessment Opportunities</h3>
	 <div class="ui-accordion-content ui-helper-reset ui-widget-content ui-corner-bottom yui-wk-div" id="ui-id-2" aria-labelledby="ui-id-1" role="tabpanel" aria-hidden="true" style="display: none;">
	   <p>You can examine students’ work on the interactive exercise and their reflection portfolio entries to assess their progress on the following learning objectives. If students are able to do what is listed there, they are ready to move on to the next lesson.</p>
	   <ul>
	     <li><i><b>Interactive Exercises:</b></i> </li>
	     <li><i><b>Portfolio Reflections:</b></i>
	         <br>LO X.X.X - Students should be able to ...
	     </li>
	     <li><i><b>In the XXX App, look for:</b></i>
	     </li>
	   </ul>
	 </div>
	 
	 <h3 class="diff-practice ui-accordion-header ui-state-default ui-corner-all" role="tab" id="ui-id-3" aria-controls="ui-id-4" aria-selected="false" aria-expanded="false" tabindex="-1">Differentiation: More Practice</h3>
	 <div class="ui-accordion-content ui-helper-reset ui-widget-content ui-corner-bottom yui-wk-div" id="ui-id-4" aria-labelledby="ui-id-3" role="tabpanel" aria-hidden="true" style="display: none;">
	   <p>Have students review the mini-lessons on data persistence on AppInventor.org: <a href="http://www.appinventor.org/content/howDoYou/persistence" target="_blank">How Do You? Store Data Persistently</a></p>
	 </div>
	 
	 <h3 class="diff-enrich ui-accordion-header ui-state-default ui-corner-all" role="tab" id="ui-id-5" aria-controls="ui-id-6" aria-selected="false" aria-expanded="false" tabindex="-1">Differentiation: Enrichment</h3>
	 <div class="ui-accordion-content ui-helper-reset ui-widget-content ui-corner-bottom yui-wk-div" id="ui-id-6" aria-labelledby="ui-id-5" role="tabpanel" aria-hidden="true" style="display: none;">
	   <p>Students could explore using the TinyDb component to store the last color selected.</p>
	 </div>
	
	 <h3 class="bk-knowledge ui-accordion-header ui-state-default ui-corner-all" role="tab" id="ui-id-7" aria-controls="ui-id-8" aria-selected="false" aria-expanded="false" tabindex="-1">Background Knowledge: TinyDB</h3>
	 <div class="ui-accordion-content ui-helper-reset ui-widget-content ui-corner-bottom yui-wk-div" id="ui-id-8" aria-labelledby="ui-id-7" role="tabpanel" aria-hidden="true" style="display: none;">
	   <p>TinyDB only stores data on the device, which is cost efficient, but doesn't allow sharing of data between devices. Also, the size and the amount of data that can be stored will be limited with a TinyDB. This should lead into the topic of a TinyWebDB in an upcoming lesson, which allows for the sharing of data via the web.</p>
	   <p><a href="http://ai2.appinventor.mit.edu/reference/components/storage.html#TinyDB" target="_blank">AI2 Documentation on Tiny DB</a></p>
	 </div>
	
	 
	</div> <!-- accordion -->
	
	<div class="pd yui-wk-div">

Professional Development Reflection
----------------------------------------------

.. raw:: html

	 <p>Discuss the following questions with other teachers in your professional development program.</p>
	 <ul>  
	   <li>How does this lesson reinforce the computational thinking practice of analyzing problems and artifacts? <div class="hover ctp yui-wk-div" data-id="4">[P 4]</div></li>
	 </ul>
	 
	 <!-- These are the PD exit slips.  We should have corresponding exit slips for use after the classroom lesson. -->
	 
	 <question quid="5534884309237760" weight="1" instanceid="SOaKR2qTTMFg"></question>
	 <question quid="6186819911680000" weight="1" instanceid="f7T2B6g8YJUy"></question>
	     
	</div>
