<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\App;
use Illuminate\Support\Facades\URL;
use Symfony\Component\HttpFoundation\Response;

/**
 * Reads the language from the first part of the URL (/en, /ar, /zh),
 * switches Laravel to it, and makes route() fill it in automatically.
 */
class SetLocale
{
    public function handle(Request $request, Closure $next): Response
    {
        $locale = $request->route('locale');

        if (! array_key_exists($locale, config('scil.locales'))) {
            abort(404);
        }

        App::setLocale($locale);
        URL::defaults(['locale' => $locale]);

        // Controllers do not need the {locale} parameter themselves.
        $request->route()->forgetParameter('locale');

        return $next($request);
    }
}
