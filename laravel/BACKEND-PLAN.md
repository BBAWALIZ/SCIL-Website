# Phase 2: back end (plan)

The front end is done. This is the proposed scope for the back end, for the IT team to estimate and confirm with SCIL management before work starts.

## Goals

1. **Never lose an enquiry.** Today the form only opens the visitor's email app or WhatsApp. If they don't press send, the lead is gone.
2. **Let SCIL staff edit content** (machines, prices, photos, testimonials, team) without a developer.
3. Keep the site fast and simple to host.

## Proposed scope

### 2.1 Database
- MySQL 8 (or MariaDB 10.6+). Set `DB_CONNECTION=mysql` in `.env`.
- Switch `SESSION_DRIVER` and `CACHE_STORE` to `database` (or Redis) once the database exists.

### 2.2 Enquiries (highest priority)
- Table `enquiries`: product, container size, output, machine, name, country, reply contact, notes, language, page URL, UTM source, IP/country, status (new / contacted / quoted / won / lost), assigned salesperson, timestamps.
- `POST /{locale}/enquiry` → `EnquiryController@store` with validation, CSRF, a honeypot field and rate limiting (`throttle:5,1`).
- On save: email to info@ (and the right salesperson by language or country), using Laravel Mail through SMTP or a mail service.
- The form keeps the WhatsApp button. The "Send by email" button becomes a real "Send" that posts to the server, then shows a thank-you message in the visitor's language.
- Optional: send new leads to a CRM or Google Sheet through a webhook.

### 2.3 Admin panel
- Suggested: **Filament** (free Laravel admin panel) at `/admin`, behind login with two-factor.
- Screens: Enquiries (list, filter, status, export CSV), Machines, Stations, SOLO, Testimonials, Team, Client logos, Site settings (phones, emails, address).
- Each text field has three language tabs (EN / AR / ZH). Suggested package: `spatie/laravel-translatable`.
- Image upload with automatic resizing to WebP.

### 2.4 Moving content from files to the database
- Write a seeder that reads today's `config/scil.php` and `lang/*/*.php` and fills the tables, so nothing is retyped.
- Change only `app/Support/Catalog.php` to read from the database (with caching). The views and controllers stay as they are, because they already get their data from `Catalog`.
- UI words such as button labels stay in `lang/*/ui.php` and `lang/*/pages.php`, since they rarely change.

### 2.5 SEO and tracking
- `sitemap.xml` generated from the machine list (all three languages, with hreflang).
- Redirect map from old scil-machinery.com URLs (see README checklist).
- Analytics: Google Analytics doesn't load reliably in mainland China. Consider Baidu Tongji for `/zh`, or a self-hosted tool such as Plausible or Matomo for all languages.

### 2.6 Operations
- Daily database backup.
- Error logging (log file plus an email on errors, or a service such as Sentry).
- `php artisan test` in CI on every push.

## Not in scope (unless asked)
- Online payment or a shop for SOLO machines (prices are published, but orders go through sales).
- Customer login or portal.
