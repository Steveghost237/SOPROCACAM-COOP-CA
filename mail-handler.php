<?php
/**
 * SOPROCACAM COOP-CA — Gestionnaire de formulaires
 * Envoie un email HTML stylé vers info@soprocacam.com
 */
ob_start();
error_reporting(0);
ini_set('display_errors', 0);

header('Content-Type: application/json; charset=utf-8');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    ob_end_clean();
    http_response_code(405);
    echo json_encode(['success' => false]);
    exit;
}

if (!empty($_POST['_trap'])) {
    ob_end_clean();
    echo json_encode(['success' => true]);
    exit;
}

function clean(string $v): string {
    return htmlspecialchars(trim(strip_tags($v)), ENT_QUOTES, 'UTF-8');
}

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

$nom_exp = ($type === 'partenaire') ? $nom_complet : trim("$prenom $nom");

// Validation : nom obligatoire, email requis uniquement si fourni
if (empty($nom_exp)) {
    ob_end_clean();
    http_response_code(400);
    echo json_encode(['success' => false]);
    exit;
}
$email_valide = filter_var($email, FILTER_VALIDATE_EMAIL);
if (!$email_valide) { $email = ''; }

/* ---------- Date ---------- */
$jours = ['Dimanche','Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi'];
$mois  = ['Janvier','Février','Mars','Avril','Mai','Juin',
          'Juillet','Août','Septembre','Octobre','Novembre','Décembre'];
$date_fr = $jours[(int)date('w')] . ' ' . date('d') . ' '
         . $mois[(int)date('n') - 1] . ' ' . date('Y') . ' à ' . date('H:i');

/* ---------- Sujet ---------- */
$to      = 'info@soprocacam.com';
$subject = ($type === 'partenaire')
    ? "Demande de partenariat — $nom_exp | SOPROCACAM"
    : "Demande de devis — $nom_exp | SOPROCACAM";

/* ---------- Lignes du tableau ---------- */
if ($type === 'partenaire') {
    $rows = [
        ['Nom et prénom',     $nom_complet],
        ['Téléphone',         $telephone ?: '—'],
        ['E-mail',            $email ?: '—'],
        ['Localité / Région', $localite ?: '—'],
        ['Profil',            $vous_etes ?: '—'],
        ['Message',           $message ? nl2br($message) : '—'],
    ];
} else {
    $rows = [
        ['Prénom',            $prenom],
        ['Nom',               $nom],
        ['Entreprise',        $entreprise ?: '—'],
        ['Pays',              $pays ?: '—'],
        ['E-mail',            $email ?: '—'],
        ['Téléphone',         $telephone ?: '—'],
        ['Produit souhaité',  $produit ?: '—'],
        ['Quantité',          $quantite ?: '—'],
        ['Destination',       $destination ?: '—'],
        ['Message',           $message ? nl2br($message) : '—'],
    ];
}

$rows_html = '';
foreach ($rows as [$label, $value]) {
    $rows_html .=
        '<tr>'
        . '<td style="padding:10px 16px;background:#fdf6ef;color:#C8953A;font-weight:700;'
        . 'font-size:11px;text-transform:uppercase;letter-spacing:.5px;'
        . 'border-bottom:1px solid #f0e0cc;white-space:nowrap;width:170px;">'
        . htmlspecialchars($label, ENT_QUOTES, 'UTF-8')
        . '</td>'
        . '<td style="padding:10px 16px;color:#2d2d2d;font-size:14px;'
        . 'border-bottom:1px solid #f0e0cc;line-height:1.6;">'
        . $value
        . '</td></tr>';
}

$badge_bg   = ($type === 'partenaire') ? '#2E7D32' : '#512616';
$type_label = ($type === 'partenaire') ? 'Demande de partenariat' : 'Demande de devis / Contact';

/* ---------- Template HTML ---------- */
$html = '<!DOCTYPE html><html lang="fr"><head><meta charset="UTF-8"></head>'
. '<body style="margin:0;padding:0;background:#f4f1ee;font-family:Arial,sans-serif;">'
. '<table width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#f4f1ee;padding:32px 16px;">'
. '<tr><td align="center">'
. '<table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;width:100%;border-radius:12px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,.12);">'

// EN-TÊTE
. '<tr><td style="background:#512616;padding:32px 40px;text-align:center;">'
. '<table width="64" cellpadding="0" cellspacing="0" border="0" style="margin:0 auto 16px;"><tr><td style="width:64px;height:64px;background:rgba(255,255,255,.15);border-radius:32px;border:3px solid rgba(255,255,255,.3);text-align:center;vertical-align:middle;">'
. '<span style="color:#C8953A;font-size:28px;font-weight:900;">S</span>'
. '</td></tr></table>'
. '<h1 style="margin:0;color:#fff;font-size:22px;font-weight:700;letter-spacing:.5px;">SOPROCACAM COOP-CA</h1>'
. '<p style="margin:6px 0 0;color:rgba(255,255,255,.75);font-size:12px;">Trader &amp; Exportateur agr&eacute;&eacute; &mdash; Membre du GEX &mdash; Douala, Cameroun</p>'
. '</td></tr>'

// BADGE
. '<tr><td style="background:#fff;padding:20px 40px 0;text-align:center;">'
. '<span style="display:inline-block;background:' . $badge_bg . ';color:#fff;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;padding:6px 20px;border-radius:20px;">' . $type_label . '</span>'
. '</td></tr>'

// DATE
. '<tr><td style="background:#fff;padding:14px 40px 20px;">'
. '<p style="margin:0;font-size:13px;color:#777;border-left:3px solid #C8953A;padding-left:12px;line-height:1.7;">'
. 'Re&ccedil;u le <strong>' . $date_fr . '</strong> via '
. '<a href="https://www.soprocacam.com" style="color:#512616;text-decoration:none;">www.soprocacam.com</a>'
. '</p></td></tr>'

// DONNÉES
. '<tr><td style="background:#fff;padding:0 40px 32px;">'
. '<table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-radius:8px;overflow:hidden;border:1px solid #f0e0cc;">'
. $rows_html
. '</table></td></tr>'

// BOUTON
. '<tr><td style="background:#fdf6ef;padding:24px 40px;text-align:center;border-top:2px solid #f0e0cc;">'
. '<p style="margin:0 0 14px;color:#512616;font-size:14px;font-weight:700;">R&eacute;pondre &agrave; cette demande&nbsp;:</p>'
. '<a href="mailto:' . $email . '" style="display:inline-block;background:#512616;color:#fff;text-decoration:none;font-size:13px;font-weight:700;padding:13px 30px;border-radius:6px;letter-spacing:.5px;">'
. '&#9993;&nbsp; R&eacute;pondre &agrave; ' . htmlspecialchars($nom_exp, ENT_QUOTES, 'UTF-8')
. '</a></td></tr>'

// PIED DE PAGE
. '<tr><td style="background:#3a1a0a;padding:22px 40px;text-align:center;">'
. '<p style="margin:0 0 6px;color:rgba(255,255,255,.8);font-size:12px;"><strong style="color:#C8953A;">SOPROCACAM COOP-CA</strong> &mdash; Immeuble AXA, rue 309 (rue Franqueville), Akwa, BP&nbsp;6469, Douala, Cameroun</p>'
. '<p style="margin:0;color:rgba(255,255,255,.55);font-size:11px;">+237&nbsp;673&nbsp;33&nbsp;01&nbsp;01 &nbsp;|&nbsp;<a href="mailto:info@soprocacam.com" style="color:#C8953A;">info@soprocacam.com</a>&nbsp;|&nbsp;<a href="https://www.soprocacam.com" style="color:#C8953A;">www.soprocacam.com</a></p>'
. '<p style="margin:10px 0 0;color:rgba(255,255,255,.3);font-size:10px;">Message g&eacute;n&eacute;r&eacute; automatiquement par le formulaire du site web SOPROCACAM.</p>'
. '</td></tr>'

. '</table></td></tr></table>'
. '</body></html>';

/* ---------- Envoi ---------- */
$headers  = "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/html; charset=UTF-8\r\n";
$headers .= "From: SOPROCACAM Site <info@soprocacam.com>\r\n";
if ($email) { $headers .= "Reply-To: $email\r\n"; }
$headers .= "X-Mailer: PHP/" . PHP_VERSION . "\r\n";

ob_end_clean();

$sent = @mail($to, '=?UTF-8?B?' . base64_encode($subject) . '?=', $html, $headers);

echo json_encode(['success' => (bool)$sent]);
