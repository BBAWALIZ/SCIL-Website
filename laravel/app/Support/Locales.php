<?php

namespace App\Support;

use Illuminate\Support\Facades\Route;

/** Language helpers for the views. */
class Locales
{
    /** Every language: code => [name, dir, og, html]. */
    public static function all(): array
    {
        return config('scil.locales');
    }

    public static function current(): array
    {
        return self::all()[app()->getLocale()] + ['code' => app()->getLocale()];
    }

    /** The same page in another language, or that language's home page. */
    public static function url(string $locale): string
    {
        $route = Route::current();

        if ($route && $route->getName()) {
            return route($route->getName(), array_merge($route->parameters(), ['locale' => $locale]));
        }

        return url("/$locale");
    }

    /** Value for <html lang="">. */
    public static function htmlLang(?string $locale = null): string
    {
        $locale ??= app()->getLocale();

        return self::all()[$locale]['html'] ?? $locale;
    }
}
