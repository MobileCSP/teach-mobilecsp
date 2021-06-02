.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Where is North: A Compass App (Optional)
=========================================

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
	     generateFrameworkTable(EKmapping['9.07']);
	     generateHovers();
	 }); 
	
	</script>
	
	<!-- This is the overview paragraph.  The link URL should be to the corresponding lesson on the student branch. -->
	<p class="overview">
	 <a href="https://course.mobilecsp.org/mobilecsp/unit?unit=149&amp;lesson=103" target="_blank" title="">This lesson</a> provides an introduction to the Global Positioning System (GPS) as well as how to handle the complexity of many different screen sizes when designing mobile apps. It reinforces the enduring understandings of writing programs to execute algorithms, such as computing the center of a screen's width, as well as demonstrates how the GPS system in the app allows users to interact with their environment. The follow-up lesson is the My Directions Tutorial in Unit 7 which covers how to build an app that uses a Location sensor and Google Maps to get directions from a current location. The Walking Tour app in Unit 3 also reinforces the concept of GPS and identifying locations on a map.
	</p>
	
	<!-- This is the framework table, where we describe how this lesson fits into the CSP framework.  --> 
	<table border id="genTable" class="framework" width="100%"></table>
	<!--   End of Framework table. -->
	
	
	<!-- This div associates the teach branch with the corresponding student branch. It should go after the table. -->  
	
	<div class="pd yui-wk-div">
	 <h4>PROFESSIONAL DEVELOPMENT</h4> 
	 <p><b>The Student Lesson: </b> Complete the activities for 
	   <a href="https://course.mobilecsp.org/mobilecsp/unit?unit=149&amp;lesson=103" target="_blank" title="">Mobile CSP Lesson 9.7: Where is North? A Compass App</a>.
	 </p>
	</div>
	
	<h3>Materials</h3>
	<p></p>
	<ul>
	  <li>The sensors require a device (phone or tablet) to test rather than the emulator. (The OrientationSensor does not work currently on the emulator.) Also, it looks like not all tablets will have the hardware sensors needed.</li>
	  <li><a href="https://docs.google.com/a/css.edu/document/d/1y42nrd-8UTpWMZSa7r7MN81lON1r_FVjHAQYGkN_OU8/edit" target="_blank">Location Sensor Tester App</a></li>
	  <li><a href="https://docs.google.com/a/css.edu/document/d/1PLb8CfOCMo9njCXgOPbZIcWekrpf2RBqMiL_tcVCW7c/edit#" target="_blank">Where is North Solutions</a></li>
	</ul>
	
	<h3>Learning Activities</h3>
	<h3 style="font-style:italic; background: url(../_static/assets/img/time.png) left center no-repeat; background-size:1.5em 1.5em; padding-left:2em;">Estimated Length: 45 minutes</h3>
	<p></p>
	<ul>
	  <li><b>Hook/Motivation (10 minutes):</b> Have the students brainstorm apps that use their location. Discuss what makes an app location aware.</li>
	  <li><b>Experiences and Explorations (20 minutes):</b> 
	      <ul>
	          <li>Have students try using the Location Sensor Tester app. This is a very simple example of an app that has location awareness. It requires no coding.</li>
	          <li>Lead the students through the Where is North Tutorial, which explains how to use the orientation sensor and location sensor to determine which direction North is in, as with a compass.
	During the walk-through explain that sensors in mobile devices facilitate new ways of interacting with the environment. 
	During the walk-through explain that GPS stands for Global Positioning System. Explain to the students that GPS has changed how humans travel, navigate, and find information.</li>
	      </ul>
	  </li>
	  <li><b>Rethink, Reflect and/or Revise (10 minutes):</b> Review how to use the orientation and location sensors. Students should write a reflection in their portfolio (this may be assigned for homework). Have students try the interactive exercises on location awareness.</li>
	</ul>
	
	<h3>Assessment/Evidence</h3>
	<p>Formative Assessment: Interactive exercises on the Mobile CSP lesson page</p>
	
	<div class="pd yui-wk-div">
	 <h4>PROFESSIONAL DEVELOPMENT - Background Knowledge</h4> 
	 <p><a href="http://ai2.appinventor.mit.edu/reference/components/sensors.html" target="_blank">Read more</a> about the App Inventor Location and Orientation sensors.
	 </p>
	 <p><b>Directional Bugs</b>: As some of you are noticing, and as others have noticed in the past, there is a bug in the "Where is North" app.  The azimuth correction — adding 90 — doesn't work well for other directions besides North. The reason is that the sprite heading changes from 0 to 360 in a clockwise direction, whereas the azimuth changes from 0 to 360 in a counter-clockwise direction. Alan Tranciato (Meriden High School, Meriden CT) has created a nice fix for this — i.e., he wrote a procedure that converts azimuth to heading. (Procedures are covered in Unit 5.)<br>
	 <img width="647" src="../_static/assets/img/TransformAzimuthFunction.png">
	 </p>
	</div>
	
	<div class="pd yui-wk-div">

Teacher PD Reflection
-----------------------

.. raw:: html

	 <p>Discuss the following questions with other teachers in your professional development program.</p>
	 <ul>    
	   <li>How does this lesson help students toward the enduring understanding that people write programs to implement algorithms? 
	     <div class="hover eu yui-wk-div" data-id="5.2">[EU 5.2]</div>
	   </li>
	   <li>How does this lesson help students toward the enduring understanding that computing enhances communication, interaction, and cognition? 
	     <div class="hover eu yui-wk-div" data-id="7.1">[EU 7.1]</div>
	   </li> 
	   <li>How does this lesson help students develop the computational thinking practice of analyzing problems and artifacts? 
	     <div class="hover ctp yui-wk-div" data-id="4">[P 4]</div>
	   </li>    
	 </ul>
	 
	 <!-- These are the PD exit slips.  We should have corresponding exit slips for use after the classroom lesson. -->
	 <p>
	   <question quid="5977117141499904" weight="0" instanceid="Mdhmeur1I0pl">
	   </question>
	   <br>
	   <question quid="5131993071222784" weight="0" instanceid="vuq1LbbAWCq2">
	   </question>
	 </p>
	</div>

	
