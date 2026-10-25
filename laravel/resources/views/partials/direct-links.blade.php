{{-- Direct contact links beside a form. $items: list of whatsapp|call|call_short|email|catalogue|parts --}}
@php $c = config('scil.contact'); @endphp
<div class="zone__direct">
@foreach ($items as $item)
  @switch($item)
    @case('whatsapp')
      <a href="https://wa.me/{{ $c['whatsapp'] }}" rel="noopener"><x-icon name="chat"/> {{ __('ui.dl_whatsapp') }} <span class="data" dir="ltr">{{ $c['whatsapp_display'] }}</span></a>
      @break
    @case('call')
    @case('call_short')
      <a href="{{ $c['phone_href'] }}"><x-icon name="phone"/> {{ __('ui.dl_'.$item) }} <span class="data" dir="ltr">{{ $c['phone'] }}</span></a>
      @break
    @case('email')
      <a href="mailto:{{ $c['email'] }}"><x-icon name="mail"/> {{ __('ui.dl_email') }} <span class="data">{{ $c['email'] }}</span></a>
      @break
    @case('catalogue')
      <a href="{{ $c['catalogue'] }}" rel="noopener"><x-icon name="download"/> {{ __('ui.dl_catalogue') }} <span class="data">PDF</span></a>
      @break
    @case('parts')
      <a href="mailto:{{ $c['email_parts'] }}"><x-icon name="mail"/> {{ __('ui.dl_parts') }} <span class="data">{{ $c['email_parts'] }}</span></a>
      @break
  @endswitch
@endforeach
</div>
