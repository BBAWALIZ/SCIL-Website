@php
    use App\Support\Locales;
    $c = config('scil.contact');
    $catalog = app(\App\Support\Catalog::class);
    $others = array_diff_key(Locales::all(), [app()->getLocale() => true]);
@endphp
<footer class="footer">
  <div class="wrap">
    <div class="footer__grid">
      <div>
        <p class="footer__big">{!! __('ui.footer_big') !!}</p>
        <address>{{ __('ui.hq') }}<br>{!! implode('<br>', array_map('e', $c['address'])) !!}</address>
        <div class="footer__qr">
          <img src="{{ asset('assets/img/brand/wechat-qr.jpg') }}" alt="{{ __('ui.qr_alt') }}" width="92" height="92" loading="lazy">
          <p class="meta" style="margin:0">{!! __('ui.qr_txt') !!}</p>
        </div>
      </div>
      <div>
        <h2>{{ __('ui.talk') }}</h2>
        <ul>
          <li><a href="{{ $c['phone_href'] }}" dir="ltr">{{ $c['phone'] }}</a></li>
          <li><a href="https://wa.me/{{ $c['whatsapp'] }}" rel="noopener">{{ __('ui.whatsapp') }} <span dir="ltr">{{ $c['whatsapp_display'] }}</span></a></li>
          <li><a href="mailto:{{ $c['email'] }}">{{ $c['email'] }}</a></li>
          <li><a href="mailto:{{ $c['email_sales'] }}">{{ $c['email_sales'] }}</a></li>
        </ul>
        <h2 style="margin-top:28px">{{ __('ui.agent') }}</h2>
        <p style="margin:0">{!! __('ui.agent_txt') !!}</p>
      </div>
      <div>
        <h2>{{ __('ui.the_line') }}</h2>
        <ul>
          @foreach ($catalog->stations() as $s)
            <li><a href="{{ route('equipment') }}#{{ $s['key'] }}">{{ $s['no'] }} {{ $s['name'] }}</a></li>
          @endforeach
          <li><a href="{{ route('equipment') }}#water-treatment">{{ __('ui.water') }}</a></li>
        </ul>
      </div>
      <div>
        <h2>{{ __('ui.company') }}</h2>
        <ul>
          <li><a href="{{ route('services') }}">{!! __('ui.f_links.services') !!}</a></li>
          <li><a href="{{ route('solo') }}">{{ __('ui.f_links.solo') }}</a></li>
          <li><a href="{{ route('about') }}">{{ __('ui.f_links.about') }}</a></li>
          <li><a href="{{ route('contact') }}">{{ __('ui.f_links.contact') }}</a></li>
          <li><a href="{{ $c['catalogue'] }}" rel="noopener">{{ __('ui.f_links.catalogue') }}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__base">
      <span>{{ __('ui.rights', ['year' => date('Y')]) }}</span>
      <nav aria-label="{{ __('ui.language') }}">
        @foreach ($others as $code => $l)
          <a href="{{ Locales::url($code) }}" lang="{{ Locales::htmlLang($code) }}" hreflang="{{ Locales::htmlLang($code) }}">{{ $l['name'] }}</a>
        @endforeach
      </nav>
      <div class="social">
        @foreach (config('scil.social') as $s)
          <a href="{{ $s['url'] }}" rel="noopener" target="_blank" aria-label="{{ $s['name'] }}"><x-icon :name="$s['icon']"/></a>
        @endforeach
      </div>
    </div>
  </div>
</footer>
