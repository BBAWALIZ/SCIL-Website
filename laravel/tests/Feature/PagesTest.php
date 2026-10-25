<?php

namespace Tests\Feature;

use Tests\TestCase;

/**
 * Opens every page in every language and checks it loads.
 * Run with: php artisan test
 */
class PagesTest extends TestCase
{
    public function test_root_redirects_to_a_language(): void
    {
        $this->get('/')->assertRedirect('/en');
        $this->withHeader('Accept-Language', 'ar-SA,ar;q=0.9')->get('/')->assertRedirect('/ar');
        $this->withHeader('Accept-Language', 'zh-CN,zh;q=0.9')->get('/')->assertRedirect('/zh');
    }

    public function test_every_page_loads_in_every_language(): void
    {
        $pages = ['', '/equipment', '/services', '/solo', '/about', '/contact'];
        foreach (array_keys(config('scil.locales')) as $locale) {
            foreach ($pages as $page) {
                $this->get("/$locale$page")->assertOk()->assertSee('SCIL');
            }
        }
    }

    public function test_every_machine_page_loads_in_every_language(): void
    {
        foreach (array_keys(config('scil.locales')) as $locale) {
            foreach (config('scil.machines') as $id => $m) {
                $this->get("/$locale/equipment/{$m['slug']}")
                    ->assertOk()
                    ->assertSee(trans("machines.$id.name", [], $locale));
            }
        }
    }

    public function test_every_language_has_every_machine_and_solo_item(): void
    {
        foreach (array_keys(config('scil.locales')) as $locale) {
            foreach (array_keys(config('scil.machines')) as $id) {
                $this->assertNotEmpty(trans("machines.$id.name", [], $locale), "$locale machine $id");
            }
            $this->assertCount(count(config('scil.solo')), trans('solo', [], $locale), "$locale solo");
        }
    }

    public function test_arabic_pages_are_right_to_left(): void
    {
        $this->get('/ar')->assertSee('dir="rtl"', false);
        $this->get('/zh')->assertSee('lang="zh-Hans"', false);
    }

    public function test_unknown_pages_return_404(): void
    {
        $this->get('/en/equipment/no-such-machine')->assertNotFound();
        $this->get('/fr')->assertNotFound();
    }

    public function test_old_static_addresses_redirect(): void
    {
        $this->get('/index.html')->assertRedirect('/en');
        $this->get('/ar/equipment.html')->assertRedirect('/ar/equipment');
        $this->get('/equipment/juice-filling-machine.html')->assertRedirect('/en/equipment/juice-filling-machine');
    }
}
