@php
    use App\Support\Locales;
    $c = config('scil.contact');
    $others = array_diff_key(Locales::all(), [app()->getLocale() => true]);
@endphp
<header class="gantry" data-gantry>
  <div class="wrap gantry__in">
    <a class="brand" href="{{ route('home') }}" aria-label="{{ __('ui.home_label') }}">
      <span class="brand__plate"><img src="{{ asset('assets/img/brand/logo350.png') }}" alt="SCIL" width="77" height="34"></span>
      <span class="brand__txt">{!! __('ui.brand_txt') !!}</span>
    </a>
    <nav aria-label="{{ __('ui.menu') }}"><ul class="zones" id="zones">
      @foreach (__('ui.nav') as $key => $label)
        <li><a href="{{ route($key) }}" @if($active === $key) aria-current="page" @endif>{{ $label }}</a></li>
      @endforeach
      @foreach ($others as $code => $l)
        <li class="lang-li"><a href="{{ Locales::url($code) }}" lang="{{ Locales::htmlLang($code) }}" hreflang="{{ Locales::htmlLang($code) }}">{{ $l['name'] }}</a></li>
      @endforeach
    </ul></nav>
    <div class="gantry__call">
      <span class="langs" aria-label="{{ __('ui.language') }}">
        @foreach ($others as $code => $l)
          <a class="lang-switch" href="{{ Locales::url($code) }}" lang="{{ Locales::htmlLang($code) }}" hreflang="{{ Locales::htmlLang($code) }}">{{ $l['name'] }}</a>
        @endforeach
      </span>
      <a class="gantry__tel" href="{{ $c['phone_href'] }}" dir="ltr">{{ $c['phone'] }}</a>
      <a class="btn btn--small" href="{{ route('contact') }}">{{ __('ui.cta') }} <x-icon name="arrow"/></a>
    </div>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="zones" data-menu>
      <span class="visually-hidden">{{ __('ui.menu') }}</span><x-icon name="menu" class="i-open"/>
    </button>
  </div>
</header>
