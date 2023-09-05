<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $uploadDir = "uploads/"; // Yüklenen dosyaların kaydedileceği klasör
    $blockedExtensions = ["php"]; // Engellenen dosya uzantıları

    $fileName = $_FILES["file"]["name"];
    $fileExtension = strtolower(pathinfo($fileName, PATHINFO_EXTENSION));

    if (!in_array($fileExtension, $blockedExtensions)) {
        $uploadPath = $uploadDir . basename($fileName);

        if (move_uploaded_file($_FILES["file"]["tmp_name"], $uploadPath)) {
            echo "Dosya başarıyla yüklendi.";
        } else {
            echo "Dosya yüklenirken bir hata oluştu.";
        }
    } else {
        echo "Geçersiz dosya uzantısı. .php uzantılı dosyalar yasaklanmıştır.";
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Fotoğraf Yükleme</title>
</head>
<body>
    <h2>Fotoğraf Yükleme</h2>
    <form action="" method="POST" enctype="multipart/form-data">
        Dosya seçin: <input type="file" name="file">
        <input type="submit" value="Yükle">
    </form>
</body>
</html>
