@props(['name', 'class' => '', 'label' => null])
{{-- A container drawing from the sprite in partials/sprite.blade.php --}}
<svg class="{{ $class }}" viewBox="0 0 300 400" @if($label) role="img" aria-label="{{ $label }}" @else aria-hidden="true" @endif><use href="#tk-{{ $name }}"/></svg>
