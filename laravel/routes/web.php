<?php

use App\Http\Controllers\PageController;
use App\Http\Middleware\SetLocale;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Pages
|--------------------------------------------------------------------------
| Every page lives under its language: /en/..., /ar/..., /zh/...
*/

$locales = implode('|', array_keys(config('scil.locales')));

// The bare domain sends visitors to the language their browser asks for.
Route::get('/', function (Request $request) {
    $locale = $request->getPreferredLanguage(array_keys(config('scil.locales'))) ?? 'en';

    return redirect("/$locale", 302);
});

Route::prefix('{locale}')
    ->where(['locale' => $locales])
    ->middleware(SetLocale::class)
    ->group(function () {
        Route::get('/', [PageController::class, 'home'])->name('home');
        Route::get('/equipment', [PageController::class, 'equipment'])->name('equipment');
        Route::get('/equipment/{slug}', [PageController::class, 'machine'])
            ->where('slug', '[a-z0-9-]+')->name('machine');
        Route::get('/services', [PageController::class, 'services'])->name('services');
        Route::get('/solo', [PageController::class, 'solo'])->name('solo');
        Route::get('/about', [PageController::class, 'about'])->name('about');
        Route::get('/contact', [PageController::class, 'contact'])->name('contact');
    });

/*
|--------------------------------------------------------------------------
| Old addresses
|--------------------------------------------------------------------------
| Links to the previous static site (index.html, ar/equipment.html,
| equipment/<machine>.html ...) are sent to the new pages permanently.
| Add the old scil-machinery.com addresses here too before launch.
*/

Route::get('{path}', function (string $path) use ($locales) {
    if (! preg_match("#^(?:($locales)/)?(index|equipment|services|solo|about|contact)?(?:/([a-z0-9-]+))?\.html$#", $path, $m)) {
        abort(404);
    }
    $locale = $m[1] ?: 'en';
    $page = ($m[2] ?? '') ?: 'index';
    $slug = $m[3] ?? null;

    $url = match (true) {
        $page === 'equipment' && $slug !== null => route('machine', ['locale' => $locale, 'slug' => $slug]),
        $page === 'index' => route('home', ['locale' => $locale]),
        default => route($page, ['locale' => $locale]),
    };

    return redirect($url, 301);
})->where('path', '.+\.html');
