<?php
/**
 * SOPROCACAM COOP-CA — Gestionnaire de formulaires
 * Envoie les demandes de contact / devis / partenariat
 * vers info@soprocacam.com avec un email HTML stylé.
 */

header('Content-Type: application/json; charset=utf-8');
header('Access-Control-Allow-Origin: https://www.soprocacam.com');
header('Access-Control-Allow-Methods: POST');

/* ---------- Sécurité ---------- */
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'message' => 'Méthode non autorisée.']);
    exit;
}

// Anti-spam honeypot
if (!empty($_POST['_trap'])) {
    echo json_encode(['success' => true]); // silently ignore bots
    exit;
}

// Sanitize helper
function clean(string $value): string {
    return htmlspecialchars(trim(strip_tags($value)), ENT_QUOTES, 'UTF-8');
}

/* ---------- Lecture des données ---------- */
$type         = clean($_POST['_form_type'] ?? 'contact');
$prenom       = clean($_POST['prenom']     ?? '');
$nom          = clean($_POST['nom']        ?? '');
$nom_complet  = clean($_POST['nom_complet'] ?? '');  // partenaire.html
$entreprise   = clean($_POST['entreprise'] ?? '');
$pays         = clean($_POST['pays']       ?? '');
$localite     = clean($_POST['localite']   ?? '');   // partenaire.html
$email        = filter_var(trim($_POST['email'] ?? ''), FILTER_SANITIZE_EMAIL);
$telephone    = clean($_POST['telephone']  ?? '');
$produit      = clean($_POST['produit']    ?? '');
$vous_etes    = clean($_POST['vous_etes']  ?? '');   // partenaire.html
$quantite     = clean($_POST['quantite']   ?? '');
$destination  = clean($_POST['destination'] ?? '');
$message      = clean($_POST['message']    ?? '');

// Validation basique
$dest_prenom  = ($type === 'partenaire') ? $nom_complet : trim("$prenom $nom");
if (empty($dest_prenom) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    http_response_code(400);
    echo json_encode(['success' => false, 'message' => 'Données invalides.']);
    exit;
}

/* ---------- Adresse destinataire ---------- */
$to      = 'info@soprocacam.com';
$from    = 'noreply@soprocacam.com';
$subject = ($type === 'partenaire')
    ? "Nouvelle demande de partenariat — $dest_prenom"
    : "Nouvelle demande de devis / contact — $dest_prenom";

/* ---------- Template HTML email ---------- */
$logo_url = 'https://www.soprocacam.com/images/logo.png';
$date_fr  = strftime('%A %d %B %Y à %H:%M', time());

// Construire le tableau de données selon le type de formulaire
if ($type === 'partenaire') {
    $rows = [
        ['Nom et prénom',       $nom_complet],
        ['Téléphone',           $telephone ?: '—'],
        ['E-mail',              $email],
        ['Localité / Région',   $localite ?: '—'],
        ['Vous êtes',           $vous_etes ?: '—'],
        ['Message',             nl2br($message) ?: '—'],
    ];
} else {
    $rows = [
        ['Prénom',              $prenom],
        ['Nom',                 $nom],
        ['Entreprise',          $entreprise ?: '—'],
        ['Pays',                $pays ?: '—'],
        ['E-mail',              $email],
        ['Téléphone',           $telephone ?: '—'],
        ['Produit souhaité',    $produit ?: '—'],
        ['Quantité souhaitée',  $quantite ?: '—'],
        ['Destination',         $destination ?: '—'],
        ['Message',             nl2br($message) ?: '—'],
    ];
}

// Générer les lignes du tableau HTML
$rows_html = '';
foreach ($rows as [$label, $value]) {
    $rows_html .= "
        <tr>
          <td style=\"padding:10px 16px;background:#fdf6ef;color:#8B5E3C;font-weight:600;
                      font-size:12px;text-transform:uppercase;letter-spacing:.6px;
                      border-bottom:1px solid #f0e0cc;white-space:nowrap;width:180px;\">
            $label
          </td>
          <td style=\"padding:10px 16px;color:#2d2d2d;font-size:14px;
                      border-bottom:1px solid #f0e0cc;line-height:1.6;\">
            $value
          </td>
        </tr>";
}

$type_label = ($type === 'partenaire') ? 'Demande de partenariat' : 'Demande de devis / Contact';
$badge_color = ($type === 'partenaire') ? '#2E7D32' : '#512616';

$html = <<<HTML
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>$subject</title>
</head>
<body style="margin:0;padding:0;background:#f4f1ee;font-family:'Helvetica Neue',Arial,sans-serif;">

  <!-- Wrapper -->
  <table width="100%" cellpadding="0" cellspacing="0" border="0"
         style="background:#f4f1ee;padding:32px 16px;">
    <tr><td align="center">

      <!-- Card -->
      <table width="600" cellpadding="0" cellspacing="0" border="0"
             style="max-width:600px;width:100%;border-radius:12px;
                    overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,.10);">

        <!-- ===== HEADER ===== -->
        <tr>
          <td style="background:#512616;padding:32px 40px;text-align:center;">
            <img src="$logo_url" alt="SOPROCACAM COOP-CA"
                 width="64" height="64"
                 style="border-radius:50%;border:3px solid rgba(255,255,255,.3);
                        margin-bottom:16px;display:block;margin-left:auto;margin-right:auto;" />
            <h1 style="margin:0;color:#fff;font-size:22px;font-weight:700;
                        letter-spacing:.5px;">SOPROCACAM COOP-CA</h1>
            <p style="margin:6px 0 0;color:rgba(255,255,255,.75);font-size:13px;">
              Trader &amp; Exportateur agréé — Membre du GEX
            </p>
          </td>
        </tr>

        <!-- ===== BADGE TYPE ===== -->
        <tr>
          <td style="background:#fff;padding:20px 40px 0;text-align:center;">
            <span style="display:inline-block;background:$badge_color;color:#fff;
                         font-size:11px;font-weight:700;text-transform:uppercase;
                         letter-spacing:1px;padding:6px 18px;border-radius:20px;">
              $type_label
            </span>
          </td>
        </tr>

        <!-- ===== INTRO ===== -->
        <tr>
          <td style="background:#fff;padding:20px 40px 24px;">
            <p style="margin:16px 0 0;color:#666;font-size:14px;line-height:1.7;
                        border-left:3px solid #C8953A;padding-left:14px;">
              Reçu le <strong>$date_fr</strong> depuis le site
              <a href="https://www.soprocacam.com" style="color:#512616;">www.soprocacam.com</a>
            </p>
          </td>
        </tr>

        <!-- ===== TABLE DONNÉES ===== -->
        <tr>
          <td style="background:#fff;padding:0 40px 32px;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0"
                   style="border-radius:8px;overflow:hidden;
                          border:1px solid #f0e0cc;">
              $rows_html
            </table>
          </td>
        </tr>

        <!-- ===== ACTION ===== -->
        <tr>
          <td style="background:#fdf6ef;padding:24px 40px;text-align:center;
                     border-top:2px solid #f0e0cc;">
            <p style="margin:0 0 16px;color:#512616;font-size:14px;font-weight:600;">
              Répondre à cette demande :
            </p>
            <a href="mailto:$email" style="display:inline-block;background:#512616;
                color:#fff;text-decoration:none;font-size:13px;font-weight:700;
                padding:12px 28px;border-radius:6px;letter-spacing:.5px;">
              Répondre à $dest_prenom
            </a>
          </td>
        </tr>

        <!-- ===== FOOTER ===== -->
        <tr>
          <td style="background:#3a1a0a;padding:24px 40px;text-align:center;">
            <p style="margin:0 0 6px;color:rgba(255,255,255,.8);font-size:12px;">
              SOPROCACAM COOP-CA — Immeuble AXA, rue 309 (rue Franqueville), Akwa, BP 6469, Douala, Cameroun
            </p>
            <p style="margin:0;color:rgba(255,255,255,.5);font-size:11px;">
              +237 673 33 01 01 &nbsp;|&nbsp;
              <a href="mailto:info@soprocacam.com" style="color:rgba(255,255,255,.6);">info@soprocacam.com</a>
              &nbsp;|&nbsp;
              <a href="https://www.soprocacam.com" style="color:rgba(255,255,255,.6);">www.soprocacam.com</a>
            </p>
            <p style="margin:12px 0 0;color:rgba(255,255,255,.3);font-size:10px;">
              Ce message a été généré automatiquement par le formulaire du site web.
            </p>
          </td>
        </tr>

      </table>
      <!-- / Card -->

    </td></tr>
  </table>

</body>
</html>
HTML;

/* ---------- Envoi de l'email ---------- */
$headers  = "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/html; charset=UTF-8\r\n";
$headers .= "From: SOPROCACAM COOP-CA <$from>\r\n";
$headers .= "Reply-To: $email\r\n";
$headers .= "X-Mailer: PHP/" . phpversion() . "\r\n";

$sent = mail($to, '=?UTF-8?B?' . base64_encode($subject) . '?=', $html, $headers);

if ($sent) {
    echo json_encode(['success' => true, 'message' => 'Votre demande a bien été envoyée.']);
} else {
    http_response_code(500);
    echo json_encode(['success' => false, 'message' => 'Erreur lors de l\'envoi. Veuillez nous contacter directement.']);
}
