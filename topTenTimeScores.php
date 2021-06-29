
<?php
	
	$command = escapeshellcmd('python toptimes.py a');
	$output = json_decode(exec($command), true);
	$outputStr = "<div class = \"flexContainerVert\">";
	for($i = 0; $i < 10; $i++)
	{
		$outputStr .= "<div>" . $output[$i][0] . "</div>";
	}
	$outputStr .= "</div>";

	echo($outputStr);
?>