@props(['title', 'desc', 'active' => null])
@php
    use App\Support\Locales;
    $loc = Locales::current();
@endphp
<!doctype html>
<html lang="{{ Locales::htmlLang() }}" dir="{{ $loc['dir'] }}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{ $title }}</title>
<meta name="description" content="{{ $desc }}">
<meta name="theme-color" content="#cfd3cd">
<meta property="og:title" content="{{ $title }}">
<meta property="og:description" content="{{ $desc }}">
<meta property="og:type" content="website">
<meta property="og:locale" content="{{ $loc['og'] }}">
<meta property="og:image" content="{{ asset('assets/img/products/m34.jpg') }}">
<link rel="canonical" href="{{ Locales::url($loc['code']) }}">
@foreach (Locales::all() as $code => $l)
<link rel="alternate" hreflang="{{ Locales::htmlLang($code) }}" href="{{ Locales::url($code) }}">
@endforeach
<link rel="alternate" hreflang="x-default" href="{{ Locales::url('en') }}">
<link rel="icon" href="{{ asset('assets/img/brand/favicon.png') }}">
<link rel="stylesheet" href="{{ asset('assets/fonts/fonts.css') }}">
<link rel="stylesheet" href="{{ asset('assets/css/site.css') }}?v={{ filemtime(public_path('assets/css/site.css')) }}">
<script>document.documentElement.classList.add('js')</script>
</head>
<body>
<a class="skip" href="#main">{{ __('ui.skip') }}</a>
@include('partials.sprite')
@include('partials.gantry', ['active' => $active])
<main id="main">
{{ $slot }}
</main>
@include('partials.footer')
<script src="{{ asset('assets/js/site.js') }}?v={{ filemtime(public_path('assets/js/site.js')) }}" defer></script>
</body>
</html>
