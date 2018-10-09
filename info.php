<html>
<head>
    <title>WSJ STOCKS</title>
</head>
<body>
<table align="center" border="1">
<thead>
        <tr>
                <th>EXCHANGE</th>
                <th>SYMBOL</th>
                <th>COMPANY</th>
                <th>VOLUME</th>
                <th>PRICE</th>
                <th>CHANGE</th>
        </tr>
</thead>
<?php
    $cnx = new mysqli('localhost', 'root', 'root', 'tester');

    if ($cnx->connect_error)
        die('Connection failed: ' . $cnx->connect_error);

    $query = 'SELECT * FROM Info';
    $cursor = $cnx->query($query);
    while ($row = $cursor->fetch_assoc()) {
        echo '<tr>';
        echo '<td>' . $row['exchge'] . '</td><td>' . $row['symbol'] . '</td><td align="center">' . $row['company'] . '</td><td>' . $row['volume'] . '</td><td> '. $row['price'] . '</td><td>' . $row['chge'] .'</td>';
        echo '</tr>';
    }

    $cnx->close();
?>
<style>
table{
background-color: #D3D3D3;}
th{
color: red;}
</style>
</table>
</body>
</html>

