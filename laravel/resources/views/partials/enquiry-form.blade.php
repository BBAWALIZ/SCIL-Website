{{--
  Enquiry form. Today it opens the visitor's email app or WhatsApp with the
  enquiry written out (see public/assets/js/site.js). In the back-end phase
  it will also POST to the server, so enquiries are saved and emailed.
--}}
@php
    $c = config('scil.contact');
    $i18n = __('ui.js') + ['email' => $c['email'], 'wa' => $c['whatsapp']];
@endphp
<form class="form" data-enquiry data-i18n="{{ json_encode($i18n, JSON_UNESCAPED_UNICODE) }}" action="mailto:{{ $c['email'] }}" method="post" enctype="text/plain" novalidate>
  <fieldset class="field full chips" data-field="product">
    <legend>{{ __('ui.f_product') }}</legend>
    @foreach (__('ui.f_products') as $i => $label)
      <label><input type="radio" name="product" value="{{ $label }}" @if($i === 0) required @endif><span>{{ $label }}</span></label>
    @endforeach
    <span class="err">{{ __('ui.f_product_err') }}</span>
  </fieldset>
  <div class="field">
    <label for="f-size">{{ __('ui.f_size') }}</label>
    <input id="f-size" name="size" placeholder="{{ __('ui.f_size_ph') }}" autocomplete="off">
  </div>
  <div class="field">
    <label for="f-out">{{ __('ui.f_out') }}</label>
    <input id="f-out" name="output" inputmode="numeric" placeholder="{{ __('ui.f_out_ph') }}">
  </div>
  <div class="field full">
    <label for="f-machine">{{ __('ui.f_machine') }}</label>
    <input id="f-machine" name="machine" value="{{ $machine ?? '' }}" placeholder="{{ __('ui.f_machine_ph') }}">
  </div>
  <div class="field" data-field="name">
    <label for="f-name">{{ __('ui.f_name') }}</label>
    <input id="f-name" name="name" autocomplete="name" required>
    <span class="err">{{ __('ui.f_name_err') }}</span>
  </div>
  <div class="field">
    <label for="f-country">{{ __('ui.f_country') }}</label>
    <input id="f-country" name="country" autocomplete="country-name">
  </div>
  <div class="field full" data-field="reply">
    <label for="f-reply">{{ __('ui.f_reply') }}</label>
    <input id="f-reply" name="reply" autocomplete="email" required dir="auto">
    <span class="err">{{ __('ui.f_reply_err') }}</span>
  </div>
  <div class="field full">
    <label for="f-notes">{{ __('ui.f_notes') }}</label>
    <textarea id="f-notes" name="notes" placeholder="{{ __('ui.f_notes_ph') }}"></textarea>
  </div>
  <div class="full form__actions">
    <button class="btn" type="submit" data-via="email">{{ __('ui.f_send_email') }} <x-icon name="mail"/></button>
    <button class="btn btn--ink" type="submit" data-via="whatsapp">{{ __('ui.f_send_wa') }} <x-icon name="chat"/></button>
  </div>
  <p class="full form__note">{{ __('ui.f_note') }}</p>
  <p class="form__status" role="status" aria-live="polite"></p>
</form>
