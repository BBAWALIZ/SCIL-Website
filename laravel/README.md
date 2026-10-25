# SCIL Machinery website (Laravel / PHP)

This is the new scil-machinery.com website, rebuilt in PHP with Laravel. It is meant to **replace the current website**. It keeps the design of the static site in this repository and adds a third language.

| | |
|---|---|
| Languages | English `/en`, Arabic `/ar` (right-to-left), Simplified Chinese `/zh` |
| Framework | Laravel 13 |
| PHP | 8.3 or newer (8.4 or 8.5 recommended) |
| Database | Not needed yet. The back-end phase adds MySQL. See [BACKEND-PLAN.md](BACKEND-PLAN.md). |
| Node / npm | Not needed. CSS, JavaScript and fonts are plain files in `public/assets`. |
| Status | **Phase 1: front end.** All pages work in all three languages. The enquiry form still opens the visitor's email app or WhatsApp. Phase 2 makes it save to the database and email the team. |

---

## 1. Server requirements

- PHP 8.3+ with the standard Laravel extensions: `ctype`, `curl`, `dom`, `fileinfo`, `filter`, `hash`, `mbstring`, `openssl`, `pcre`, `pdo`, `session`, `tokenizer`, `xml`
- Composer 2
- A web server (Nginx or Apache) whose **document root is the `public/` folder**. Never point it at the project root.
- Write access for PHP to `storage/` and `bootstrap/cache/`

## 2. Install (first time)

```bash
cd laravel
composer install --no-dev --optimize-autoloader
cp .env.example .env
php artisan key:generate
```

Then edit `.env`:

```dotenv
APP_ENV=production
APP_DEBUG=false
APP_URL=https://scil-machinery.com
```

Then cache everything for speed:

```bash
php artisan config:cache
php artisan route:cache
php artisan view:cache
```

### Try it locally first

```bash
composer install
cp .env.example .env && php artisan key:generate
php artisan serve
```

Open http://localhost:8000. You should land on `/en`. Then try `/ar` and `/zh`.

### Run the tests

```bash
php artisan test
```

The tests open every page and all 39 machine pages in all three languages, and check redirects and 404 pages. Run them after every content change.

## 3. Deploy

### Nginx

```nginx
server {
    listen 80;
    server_name scil-machinery.com www.scil-machinery.com;
    root /var/www/scil/laravel/public;

    index index.php;
    charset utf-8;

    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }

    location ~ \.php$ {
        fastcgi_pass unix:/run/php/php8.4-fpm.sock;
        fastcgi_param SCRIPT_FILENAME $realpath_root$fastcgi_script_name;
        include fastcgi_params;
    }

    location ~* \.(css|js|woff2|png|jpe?g|svg|webp)$ {
        expires 30d;
        add_header Cache-Control "public";
    }

    location ~ /\.(?!well-known).* { deny all; }
}
```

### Apache / cPanel

Point the domain's document root to `laravel/public`. The `.htaccess` file that Laravel needs is already in `public/`. If cPanel cannot change the document root, ask the host to do it. Do not copy `public/` up one level.

### Updating the live site later

```bash
git pull
composer install --no-dev --optimize-autoloader
php artisan config:cache && php artisan route:cache && php artisan view:cache
```

## 4. Before switching the domain over (checklist)

- [ ] **Spare-parts email.** The old site spells it `sevice@scil-machinery.com`. Confirm the real mailbox and fix it in `config/scil.php`.
- [ ] **Catalogue PDF.** All pages link to `https://scil-machinery.com/SCIL-Catalogue.pdf` on the old site. Copy that file to `public/SCIL-Catalogue.pdf` so the link keeps working after the switch.
- [ ] **Old URLs.** Get a list of the old site's page addresses (for example `/cn/site/index` and the old machine pages). Add redirects at the bottom of `routes/web.php` so Google rankings and old links carry over. Links to the previous static `.html` pages already redirect.
- [ ] **Chinese text review.** The Chinese was translated by AI. Have a Chinese-speaking colleague read `/zh` and the files in `lang/zh/`. Each file is marked at the top.
- [ ] **HTTPS.** Install an SSL certificate (Let's Encrypt is free).
- [ ] **Hosting in mainland China?** That requires an ICP licence. Hosting in Hong Kong, Singapore or Taiwan does not. The site already avoids Google services: fonts are self-hosted and Chinese uses system fonts, so it loads in mainland China.
- [ ] Run `php artisan test`. Then click through `/en`, `/ar` and `/zh` on a phone.

## 5. Where things are

```
laravel/
├── config/scil.php            ← Facts that are the same in every language: phone, emails, address,
│                                 machine list (slug, station, photo), SOLO prices, spec tables, team
├── lang/
│   ├── en/  ar/  zh/          ← All words, one folder per language (same files in each):
│   │   ├── ui.php             ←   header, footer, buttons, enquiry form
│   │   ├── pages.php          ←   page text for Home, Equipment, Services, About, SOLO, Contact
│   │   ├── machines.php       ←   each machine's name, headline figure, summary, description
│   │   ├── stations.php       ←   the 7 line stations (injection → palletizing, water treatment)
│   │   ├── solo.php           ←   SOLO machine names, descriptions and price labels
│   │   ├── testimonials.php   ←   client quotes
│   │   ├── specs.php          ←   spec table labels
│   │   └── team.php           ←   job titles and name spellings
├── routes/web.php             ← URLs, language prefixes, redirects from old addresses
├── app/Http/Controllers/PageController.php  ← one method per page
├── app/Http/Middleware/SetLocale.php        ← reads /en /ar /zh from the URL
├── app/Support/Catalog.php    ← combines config + language files (the back end will swap this to the database)
├── app/Support/Locales.php    ← language switch links, hreflang
├── resources/views/
│   ├── components/layout.blade.php   ← <head>, header, footer wrapper
│   ├── partials/                      ← header (gantry), footer, machine card, enquiry form, icons sprite
│   └── pages/                         ← one template per page
├── public/assets/             ← site.css, site.js, fonts, images (same files as the static site)
└── tests/Feature/PagesTest.php
```

### Common edits

| Task | Where |
|---|---|
| Change a phone number or email | `config/scil.php` → `contact` |
| Change a machine description | `lang/en/machines.php`, `lang/ar/machines.php`, `lang/zh/machines.php` (same id in each) |
| Add a machine | 1) add `id => slug, station, image` in `config/scil.php` → `machines`. 2) Put the photo in `public/assets/img/products/`. 3) Add the same id to `machines.php` in all three languages. The tests fail if a language is missing. |
| Change a SOLO price | `config/scil.php` → `solo` (the label stays in `lang/*/solo.php`) |
| Add a client logo | Drop the image into `public/assets/img/clients/`. It appears on the home page automatically. |
| Add a language | Add it to `config/scil.php` → `locales`, then copy `lang/en/` to `lang/<code>/` and translate |

Machine description lines use a simple format: a line starting with `-` becomes a bullet point, a line starting with `#` becomes a sub-heading, anything else is a paragraph.

After any edit in production, run `php artisan config:cache` (for `config/`) or `php artisan view:cache` (for views). Language files are read directly.

## 6. URLs

| Page | English | Arabic | Chinese |
|---|---|---|---|
| Home | `/en` | `/ar` | `/zh` |
| Equipment | `/en/equipment` | `/ar/equipment` | `/zh/equipment` |
| Machine | `/en/equipment/{slug}` | `/ar/equipment/{slug}` | `/zh/equipment/{slug}` |
| Services | `/en/services` | `/ar/services` | `/zh/services` |
| SOLO | `/en/solo` | `/ar/solo` | `/zh/solo` |
| About | `/en/about` | `/ar/about` | `/zh/about` |
| Contact | `/en/contact` | `/ar/contact` | `/zh/contact` |

`/` redirects to the visitor's browser language and falls back to English. Every page has `hreflang` links to its other two languages for Google.

## 7. Design

The design system is described in `../DESIGN.md` at the repository root (factory-floor marking: yellow for routes, blue for PET and water, green for finished goods, red for stops only). The Chinese version follows the Arabic approach. It drops the uppercase and tight letter-spacing that only suit Latin letters, and it adds more line height so Chinese characters don't clip. See the end of `public/assets/css/site.css`.

The static HTML site in the repository root is the old version and stays live on GitHub Pages until the switch.
