@php $c = config('scil.contact'); @endphp
<x-layout :title="__('pages.contact.title')" :desc="__('pages.contact.desc')" active="contact">

<section class="page-head">
  <div class="wrap">
    <ol class="crumbs"><li><a href="{{ route('home') }}">{{ __('ui.home_crumb') }}</a></li><li>{{ __('pages.contact.crumb') }}</li></ol>
    <div class="page-head__grid"><h1 class="sign-xl">{{ __('pages.contact.h1') }}</h1><p class="lede">{{ __('pages.contact.lede') }}</p></div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap hq">
    <div class="hq__main">@include('partials.enquiry-form', ['machine' => request()->query('machine')])</div>
    <aside class="hq__side" aria-label="{{ __('pages.contact.direct') }}">
      <a class="channel" href="https://wa.me/{{ $c['whatsapp'] }}" rel="noopener"><span class="channel__ic"><x-icon name="chat"/></span><span><b>{{ __('ui.dl_whatsapp') }}</b><span dir="ltr">{{ $c['whatsapp_display'] }}</span></span><x-icon name="arrow-ur"/></a>
      <a class="channel" href="{{ $c['phone_href'] }}"><span class="channel__ic"><x-icon name="phone"/></span><span><b>{{ __('ui.dl_call') }}</b><span dir="ltr">{{ $c['phone'] }}</span></span><x-icon name="arrow-ur"/></a>
      <a class="channel" href="mailto:{{ $c['email'] }}"><span class="channel__ic"><x-icon name="mail"/></span><span><b>{{ __('ui.dl_email') }}</b><span>{{ $c['email'] }}</span></span><x-icon name="arrow-ur"/></a>
      <a class="channel" href="mailto:{{ $c['email_parts'] }}"><span class="channel__ic"><x-icon name="grid"/></span><span><b>{{ __('ui.dl_parts') }}</b><span>{{ $c['email_parts'] }}</span></span><x-icon name="arrow-ur"/></a>
      <div class="channel" style="grid-template-columns:96px 1fr"><img src="{{ asset('assets/img/brand/wechat-qr.jpg') }}" alt="{{ __('pages.contact.wechat_alt') }}" width="96" height="96" style="width:96px;height:96px;object-fit:cover;object-position:center 38%;background:#fff;padding:4px"><span><b>{{ __('pages.contact.wechat') }}</b><span>{{ __('pages.contact.wechat_scan') }}</span></span></div>
      <div style="margin-top:36px">
        <h2 class="sign-s" style="margin-bottom:10px">{{ __('pages.contact.hq') }}</h2>
        <address class="prose" style="font-style:normal" dir="ltr">SCIL Machinery<br>{!! implode('<br>', array_map('e', $c['address'])) !!}</address>
        <p><a class="link-arrow" href="{{ $c['map'] }}" rel="noopener">{{ __('pages.contact.map') }} <x-icon name="arrow-ur"/></a></p>
        <h2 class="sign-s" style="margin:32px 0 10px">{{ __('pages.contact.agent') }}</h2>
        <p class="prose">Solution Plus<br>Mekacher Abderrahmane</p>
      </div>
    </aside>
  </div>
</section>

</x-layout>
