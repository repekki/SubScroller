<!DOCTYPE html>
<?php
$action = $_GET["action"];
$myText = $_POST["mytext"];

if($action = "save") {
  $targetFolder = "/path/to/file/"; // change path accordingly
  file_put_contents($targetFolder."mytext.txt", $myText);
}
?>
<html>
<head>
<meta charset="UTF-8">
 <title>Led Scroller</title>
</head>
<body>
  <form action="?action=save" name="myform" method="post">
    <input type=text name="mytext">
    <input type="submit" value="save">
  </form>
</body>
</html>

<?php

$api_url = 'https://content.googleapis.com/youtube/v3/channels';

$query = [
    'id' => 'channel id here', // Channel ID.
    'key' => 'api key here', // Your API Key.
    'part' => 'statistics',
];

$request_url = sprintf(
    '%s?%s',
    $api_url,
    http_build_query( $query )
);

$response_json = json_decode( file_get_contents( $request_url ) );

file_put_contents($targetFolder."subcount.txt", $response_json->items[0]->statistics->subscriberCount);

echo $response_json->items[0]->statistics->subscriberCount;

?>

</html>
