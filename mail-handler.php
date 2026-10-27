<?php
/**
 * SOPROCACAM COOP-CA — Gestionnaire de formulaires
 * Envoie les demandes vers info@soprocacam.com avec un email HTML stylé.
 */

// Supprimer tout avertissement PHP qui corromprait le JSON
ob_start();
error_reporting(0);
ini_set('display_errors', 0);

header('Content-Type: application/json; charset=utf-8');

/* ---------- Sécurité ---------- */
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    ob_end_clean();
    http_response_code(405);
    echo json_encode(['success' => false]);
    exit;
}

// Anti-spam honeypot
if (!empty($_POST['_trap'])) {
    ob_end_clean();
    echo json_encode(['success' => true]);
    exit;
}

// Sanitize
function clean(string $v): string {
    return htmlspecialchars(trim(strip_tags($v)), ENT_QUOTES, 'UTF-8');
}

/* ---------- Données du formulaire ---------- */
$type        = clean($_POST['_form_type'] ?? 'contact');
$prenom      = clean($_POST['prenom']      ?? '');
$nom         = clean($_POST['nom']         ?? '');
$nom_complet = clean($_POST['nom_complet'] ?? '');
$entreprise  = clean($_POST['entreprise']  ?? '');
$pays        = clean($_POST['pays']        ?? '');
$localite    = clean($_POST['localite']    ?? '');
$email       = filter_var(trim($_POST['email'] ?? ''), FILTER_SANITIZE_EMAIL);
$telephone   = clean($_POST['telephone']   ?? '');
$produit     = clean($_POST['produit']     ?? '');
$vous_etes   = clean($_POST['vous_etes']   ?? '');
$quantite    = clean($_POST['quantite']    ?? '');
$destination = clean($_POST['destination'] ?? '');
$message     = clean($_POST['message']     ?? '');

$dest_prenom = ($type === 'partenaire') ? $nom_complet : trim("$prenom $nom");

if (empty($dest_prenom) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    ob_end_clean();
    http_response_code(400);
    echo json_encode(['success' => false]);
    exit;
}

/* ---------- Date en français (sans strftime) ---------- */
$jours = ['Dimanche','Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi'];
$mois  = ['Janvier','Février','Mars','Avril','Mai','Juin',
          'Juillet','Août','Septembre','Octobre','Novembre','Décembre'];
$date_fr = $jours[(int)date('w')] . ' ' . date('d') . ' '
         . $mois[(int)date('n') - 1] . ' ' . date('Y') . ' à ' . date('H:i');

/* ---------- Sujet & destinataire ---------- */
$to      = 'info@soprocacam.com';
$subject = ($type === 'partenaire')
    ? "Demande de partenariat — $dest_prenom"
    : "Demande de devis / Contact — $dest_prenom";

/* ---------- Lignes du tableau ---------- */
if ($type === 'partenaire') {
    $rows = [
        ['Nom et prénom',     $nom_complet],
        ['Téléphone',         $telephone ?: '—'],
        ['E-mail',            $email],
        ['Localité / Région', $localite ?: '—'],
        ['Vous êtes',         $vous_etes ?: '—'],
        ['Message',           $message ? nl2br($message) : '—'],
    ];
} else {
    $rows = [
        ['Prénom',            $prenom],
        ['Nom',               $nom],
        ['Entreprise',        $entreprise ?: '—'],
        ['Pays',              $pays ?: '—'],
        ['E-mail',            $email],
        ['Téléphone',         $telephone ?: '—'],
        ['Produit souhaité',  $produit ?: '—'],
        ['Quantité',          $quantite ?: '—'],
        ['Destination',       $destination ?: '—'],
        ['Message',           $message ? nl2br($message) : '—'],
    ];
}

$rows_html = '';
foreach ($rows as [$label, $value]) {
    $rows_html .= '<tr>'
        . '<td style="padding:10px 16px;background:#fdf6ef;color:#8B5E3C;font-weight:600;'
        . 'font-size:12px;text-transform:uppercase;letter-spacing:.5px;'
        . 'border-bottom:1px solid #f0e0cc;white-space:nowrap;width:170px;">'
        . htmlspecialchars($label, ENT_QUOTES, 'UTF-8')
        . '</td>'
        . '<td style="padding:10px 16px;color:#2d2d2d;font-size:14px;'
        . 'border-bottom:1px solid #f0e0cc;line-height:1.6;">'
        . $value
        . '</td></tr>';
}

$type_label  = ($type === 'partenaire') ? 'Demande de partenariat' : 'Demande de devis / Contact';
$badge_color = ($type === 'partenaire') ? '#2E7D32' : '#512616';
$logo_url    = 'https://www.soprocacam.com/images/logo.png';

/* ---------- Template HTML email ---------- */
$html = '<!DOCTYPE html><html lang="fr"><head>'
. '<meta charset="UTF-8">'
. '<meta name="viewport" content="width=device-width,initial-scale=1">'
. '</head>'
. '<body style="margin:0;padding:0;background:#f4f1ee;font-family:Arial,sans-serif;">'

/* wrapper */
. '<table width="100%" cellpadding="0" cellspacing="0" border="0"'
. ' style="background:#f4f1ee;padding:32px 16px;">'
. '<tr><td align="center">'

/* card */
. '<table width="600" cellpadding="0" cellspacing="0" border="0"'
. ' style="max-width:600px;width:100%;border-radius:12px;overflow:hidden;'
. 'box-shadow:0 4px 24px rgba(0,0,0,.12);">'

/* HEADER */
. '<tr><td style="background:#512616;padding:32px 40px;text-align:center;">'
. '<img src="' . $logo_url . '" alt="SOPROCACAM" width="64" height="64"'
. ' style="border-radius:50%;border:3px solid rgba(255,255,255,.3);'
. 'display:block;margin:0 auto 16px;" />'
. '<h1 style="margin:0;color:#fff;font-size:22px;font-weight:700;letter-spacing:.5px;">'
. 'SOPROCACAM COOP-CA</h1>'
. '<p style="margin:6px 0 0;color:rgba(255,255,255,.75);font-size:13px;">'
. 'Trader &amp; Exportateur agr&eacute;&eacute; &mdash; Membre du GEX</p>'
. '</td></tr>'

/* BADGE */
. '<tr><td style="background:#fff;padding:20px 40px 0;text-align:center;">'
. '<span style="display:inline-block;background:' . $badge_color . ';color:#fff;'
. 'font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;'
. 'padding:6px 18px;border-radius:20px;">' . $type_label . '</span>'
. '</td></tr>'

/* DATE */
. '<tr><td style="background:#fff;padding:16px 40px 24px;">'
. '<p style="margin:0;color:#666;font-size:13px;line-height:1.7;'
. 'border-left:3px solid #C8953A;padding-left:14px;">'
. 'Re&ccedil;u le <strong>' . $date_fr . '</strong> depuis '
. '<a href="https://www.soprocacam.com" style="color:#512616;">www.soprocacam.com</a>'
. '</p></td></tr>'

/* TABLE */
. '<tr><td style="background:#fff;padding:0 40px 32px;">'
. '<table width="100%" cellpadding="0" cellspacing="0" border="0"'
. ' style="border-radius:8px;overflow:hidden;border:1px solid #f0e0cc;">'
. $rows_html
. '</table></td></tr>'

/* ACTION */
. '<tr><td style="background:#fdf6ef;padding:24px 40px;text-align:center;border-top:2px solid #f0e0cc;">'
. '<p style="margin:0 0 14px;color:#512616;font-size:14px;font-weight:600;">R&eacute;pondre &agrave; cette demande&nbsp;:</p>'
. '<a href="mailto:' . $email . '"'
. ' style="display:inline-block;background:#512616;color:#fff;text-decoration:none;'
. 'font-size:13px;font-weight:700;padding:12px 28px;border-radius:6px;letter-spacing:.5px;">'
. 'R&eacute;pondre &agrave; ' . htmlspecialchars($dest_prenom, ENT_QUOTES, 'UTF-8')
. '</a></td></tr>'

/* FOOTER EMAIL */
. '<tr><td style="background:#3a1a0a;padding:24px 40px;text-align:center;">'
. '<p style="margin:0 0 6px;color:rgba(255,255,255,.8);font-size:12px;">'
. 'SOPROCACAM COOP-CA &mdash; Immeuble AXA, rue 309, Akwa, BP 6469, Douala, Cameroun</p>'
. '<p style="margin:0;color:rgba(255,255,255,.55);font-size:11px;">'
. '+237 673 33 01 01 &nbsp;|&nbsp;'
. '<a href="mailto:info@soprocacam.com" style="color:rgba(255,255,255,.65);">info@soprocacam.com</a>'
. ' &nbsp;|&nbsp; '
. '<a href="https://www.soprocacam.com" style="color:rgba(255,255,255,.65);">www.soprocacam.com</a></p>'
. '<p style="margin:10px 0 0;color:rgba(255,255,255,.3);font-size:10px;">'
. 'Message g&eacute;n&eacute;r&eacute; automatiquement par le formulaire du site web.</p>'
. '</td></tr>'

/* /card /wrapper */
. '</table></td></tr></table>'
. '</body></html>';

/* ---------- Envoi ---------- */
$headers  = "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/html; charset=UTF-8\r\n";
$headers .= "From: SOPROCACAM Site <info@soprocacam.com>\r\n";
$headers .= "Reply-To: $email\r\n";
$headers .= "X-Mailer: PHP/" . PHP_VERSION . "\r\n";

$subject_encoded = '=?UTF-8?B?' . base64_encode($subject) . '?=';

// Vider le buffer avant de répondre
ob_end_clean();

$sent = @mail($to, $subject_encoded, $html, $headers);

if ($sent) {
    echo json_encode(['success' => true]);
} else {
    http_response_code(500);
    echo json_encode(['success' => false, 'error' => 'mail_failed']);
}
