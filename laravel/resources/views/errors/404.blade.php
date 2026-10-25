@php
    // Error pages run outside the language routes; pick the language from the URL.
    $seg = request()->segment(1);
    if (array_key_exists($seg, config('scil.locales'))) {
        app()->setLocale($seg);
        \Illuminate\Support\Facades\URL::defaults(['locale' => $seg]);
    } else {
        \Illuminate\Support\Facades\URL::defaults(['locale' => app()->getLocale()]);
    }
@endphp
<x-layout :title="__('pages.errors.not_found_title').' · SCIL Machinery'" :desc="__('pages.errors.not_found_text')">
<section class="page-head" style="padding-bottom:var(--space-section)">
  <div class="wrap">
    <div class="page-head__grid">
      <h1 class="sign-xl">{{ __('pages.errors.not_found_title') }}</h1>
      <div>
        <p class="lede">{{ __('pages.errors.not_found_text') }}</p>
        <p style="margin-top:28px"><a class="btn" href="{{ route('home') }}">{{ __('pages.errors.back_home') }} <x-icon name="arrow"/></a></p>
      </div>
    </div>
  </div>
</section>
</x-layout>
