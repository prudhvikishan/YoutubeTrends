
<?php
	$query = $_GET["q"];
	
	$command = 'python channelengagement.py ' . $query;
	$output = json_decode(exec($command), true);
	
	$outputStr = "<div><table style = \"width: 100%\">";
	$outputStr .= "<tr><td><h3>Channel</h3></td><td><h3>Combined Engagement Score</h3></td></tr>";
	$outputStr .= "<tr><td>" .  $query . "</td><td> " . $output . "</td></tr>";
	$outputStr .= "</table></div>";
	
	//echo $output;
	echo $outputStr;
?>