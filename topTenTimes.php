
<?php
	
	$command = escapeshellcmd('python toptimes.py');
	$output = json_decode(exec($command), true);
	$command2 = escapeshellcmd('python toptimes.py a');
	$output2 = json_decode(exec($command2), true);
	$outputStr = "<div><table style = \"width: 100%\">";
	$outputStr .= "<tr><td><h3>Time</h3></td><td><h3>Average Engagement Score</h3></td></tr>";
	for($i = 0; $i < 10; $i++)
	{
		$outputStr .= "<tr><td>" . $output[$i][0] . " </td><td>Average Score: " . $output2[$i][0] . "</td></tr>";
	}
	$outputStr .= "</div>";

	echo($outputStr);
?>